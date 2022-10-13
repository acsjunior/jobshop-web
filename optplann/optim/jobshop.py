import numpy as np
import pandas as pd
import pyomo.environ as pyo


class JobShop:
    model: pyo.ConcreteModel
    times: np.array
    routes: np.array
    start_time: pd.Timestamp
    time_unit: str
    solver_time: float
    objective: float
    is_optimal: bool

    def __init__(
        self,
        times: np.array,
        routes: np.array,
        start_time: pd.Timestamp,
        time_unit: str,
    ):
        self.times = times
        self.routes = routes
        self.start_time = start_time
        self.time_unit = time_unit
        self.solver_time = 0.0
        self.objective = 0.0
        self.is_optimal = False

        self.__generate_model()

    def __generate_model(self) -> pyo.ConcreteModel:
        m = len(self.times)
        n = len(self.times[0])
        V = np.max(np.cumsum(self.times))

        model = pyo.ConcreteModel()

        # Conjuntos e parâmetros:
        model.I = pyo.RangeSet(m)
        model.J = pyo.RangeSet(n)
        model.p = pyo.Param(model.I, model.J, initialize=lambda model, i, j: self.times[i-1][j-1])
        model.s = pyo.Param(model.I, model.J, initialize=lambda model, i, j: self.routes[i-1][j-1])

        # Variáveis de decisão:
        model.Cmax = pyo.Var()
        model.x = pyo.Var(model.I, model.J, within=pyo.NonNegativeReals)
        model.z = pyo.Var(model.J, model.I, model.I, within=pyo.Binary)

        # Função objetivo:
        def obj_rule(model):
            return model.Cmax
        model.obj = pyo.Objective(rule=obj_rule, sense=pyo.minimize)

        def constr1_rule(model, i, j):
            s_ij1 = model.s[i, j-1]
            s_ij = model.s[i, j]
            return model.x[i, s_ij] >= model.x[i, s_ij1] + model.p[i, s_ij1]
        model.constr1 = pyo.Constraint(model.I, [j for j in model.J if j >= 2], rule=constr1_rule)

        def constr2_rule(model, j, i, k):
            expr = pyo.Constraint.Skip
            if i < k:
                expr = model.x[i,j] >= model.x[k,j] + model.p[k,j] - V*model.z[j,i,k]
            return expr
        model.constr2 = pyo.Constraint(model.J, model.I, model.I, rule=constr2_rule)

        def constr3_rule(model, j, i, k):
            expr = pyo.Constraint.Skip
            if i < k:
                expr = model.x[k,j] >= model.x[i,j] + model.p[i,j] - V*(1 - model.z[j,i,k])
            return expr
        model.constr3 = pyo.Constraint(model.J, model.I, model.I, rule=constr3_rule)

        def constr4_rule(model, i):
            s_in = model.s[i, n]
            return model.Cmax >= model.x[i, s_in] + model.p[i, s_in]
        model.constr4 = pyo.Constraint(model.I, rule=constr4_rule)

        self.model = model

    def solve(self, solver="glpk"):
        result = pyo.SolverFactory(solver).solve(self.model)
        self.__get_solver_data(result)

    def get_output_data(self):

        keys = list(self.model.x.get_values().keys())
        machines = [str(k[1]) for k in keys]
        jobs = [str(k[0]) for k in keys]

        start_jobs = [v() for v in self.model.x.values()]
        start_jobs = pd.to_datetime(self.start_time) + pd.to_timedelta(
            start_jobs, unit=self.time_unit
        )

        durations = [float(self.model.p[k[0], k[1]]) for k in keys]

        end_jobs = start_jobs + pd.to_timedelta(durations, unit=self.time_unit)

        df_out = pd.DataFrame(
            {
                "Tarefa": jobs,
                "Máquina": machines,
                "Início": start_jobs,
                "Término": end_jobs,
            }
        )

        return df_out

    def __get_solver_data(self, result):
        self.solver_time = result["Solver"][0]["Time"]
        self.is_optimal = (
            result["Solver"][0]["Termination condition"].value == "optimal"
        )
        if self.is_optimal:
            self.objective = result["Problem"][0]["Lower bound"]
