import numpy as np
import pandas as pd
import pyomo.environ as pyo


class JobShop:
    model: pyo.ConcreteModel
    tempos: np.array
    rotas: np.array
    start_time: pd.Timestamp
    solver_time: float
    is_optimal: bool

    def __init__(self, tempos: np.array, rotas: np.array, start_time=pd.Timestamp):
        self.tempos = tempos
        self.rotas = rotas
        self.start_time = start_time
        self.solver_time = 0.0
        self.is_optimal = False

        self.__generate_model()

    def __generate_model(self) -> pyo.ConcreteModel:
        m = len(self.tempos)
        n = len(self.tempos[0])
        M = np.max(np.cumsum(self.tempos))

        model = pyo.ConcreteModel()

        # Conjuntos e parâmetros:
        model.I = pyo.RangeSet(m)
        model.J = pyo.RangeSet(n)
        model.t = pyo.Param(
            model.I, model.J, initialize=lambda model, i, j: self.tempos[i - 1][j - 1]
        )
        model.r = pyo.Param(
            model.I, model.J, initialize=lambda model, i, j: self.rotas[i - 1][j - 1]
        )

        # Variáveis de decisão:
        model.x = pyo.Var(model.I, model.J, within=pyo.NonNegativeReals)
        model.y = pyo.Var(model.I, model.I, model.J, within=pyo.Binary)

        # Função objetivo:
        def obj_rule(model):
            return sum(model.x[i, model.r[i, n]] for i in model.I)

        model.obj = pyo.Objective(rule=obj_rule, sense=pyo.minimize)

        def restr1_rule(model, i):
            r_i1 = model.r[i, 1]
            return model.x[i, r_i1] >= model.t[i, r_i1]

        model.restr_1 = pyo.Constraint(model.I, rule=restr1_rule)

        def restr2_rule(model, i, j):
            r_ij = model.r[i, j]
            r_ij1 = model.r[i, j + 1]
            return model.x[i, r_ij1] >= model.x[i, r_ij] + model.t[i, r_ij1]

        model.restr2 = pyo.Constraint(
            model.I, [j for j in model.J if j < n], rule=restr2_rule
        )

        def restr3_rule(model, i, k, j):
            expr = pyo.Constraint.Skip
            if i != k:
                expr = model.x[k, j] >= model.x[i, j] + model.t[k, j] - M * (
                    1 - model.y[i, k, j]
                )
            return expr

        model.restr3 = pyo.Constraint(model.I, model.I, model.J, rule=restr3_rule)

        def restr4_rule(model, i, k, j):
            expr = pyo.Constraint.Skip
            if i != k:
                expr = model.x[i, j] >= model.x[k, j] + model.t[i, j] - M * (
                    model.y[i, k, j]
                )
            return expr

        model.restr4 = pyo.Constraint(model.I, model.I, model.J, rule=restr4_rule)

        self.model = model

    def solve(self, solver="glpk"):
        result = pyo.SolverFactory(solver).solve(self.model)
        self.__get_solver_data(result)

    def get_output_data(self):

        keys = list(self.model.x.get_values().keys())
        machines = [str(k[1]) for k in keys]
        jobs = [str(k[0]) for k in keys]

        end_jobs = [v() for v in self.model.x.values()]
        end_jobs = pd.to_datetime(self.start_time) + pd.to_timedelta(end_jobs, unit="m")

        durations = [float(self.model.t[k[0], k[1]]) for k in keys]

        start_jobs = end_jobs - pd.to_timedelta(durations, unit="m")

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
