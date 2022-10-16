import numpy as np
import pandas as pd
import pyomo.environ as pyo

from jobshop_web.optim.model_base import ModelBase


class DisjunctiveJSSP2(ModelBase):
    def generate_model(self) -> pyo.ConcreteModel:
        m = len(self.times[0])
        n = len(self.times)
        V = np.sum(np.sum(self.times))

        model = pyo.ConcreteModel()

        # Conjuntos e parâmetros:
        model.J = pyo.RangeSet(n)
        model.M = pyo.RangeSet(m)
        model.p = pyo.Param(
            model.J, model.M, initialize=lambda model, j, i: self.times[j - 1][i - 1]
        )
        model.s = pyo.Param(
            model.J, model.M, initialize=lambda model, j, i: self.routes[j - 1][i - 1]
        )

        # Variáveis de decisão:
        model.Cmax = pyo.Var()
        model.x = pyo.Var(model.J, model.M, within=pyo.NonNegativeReals)
        model.z = pyo.Var(model.M, model.J, model.J, within=pyo.Binary)
        model.q = pyo.Var(model.M, model.J, model.J, within=pyo.NonNegativeReals)

        # Função objetivo:
        def obj_rule(model):
            return model.Cmax

        model.obj = pyo.Objective(rule=obj_rule, sense=pyo.minimize)

        def constr1_rule(model, j, i):
            s_ji1 = model.s[j, i - 1]
            s_ji = model.s[j, i]
            return model.x[j, s_ji] >= model.x[j, s_ji1] + model.p[j, s_ji1]

        model.constr1 = pyo.Constraint(
            model.J, [i for i in model.M if i >= 2], rule=constr1_rule
        )

        def constr2_rule(model, i, j, k):
            expr = pyo.Constraint.Skip
            if j < k:
                expr = (
                    V * model.z[i, j, k]
                    + (model.x[j, i] - model.x[k, i])
                    - model.p[k, i]
                    == model.q[i, j, k]
                )
            return expr

        model.constr2 = pyo.Constraint(model.M, model.J, model.J, rule=constr2_rule)

        def constr3_rule(model, i, j, k):
            expr = pyo.Constraint.Skip
            if j < k:
                expr = model.q[i, j, k] <= V - model.p[j, i] - model.p[k, i]
            return expr

        model.constr3 = pyo.Constraint(model.M, model.J, model.J, rule=constr3_rule)

        def constr4_rule(model, j):
            s_jm = model.s[j, m]
            return model.Cmax >= model.x[j, s_jm] + model.p[j, s_jm]

        model.constr4 = pyo.Constraint(model.J, rule=constr4_rule)

        self.model = model

    def get_output_data(self):

        keys = list(self.model.x.get_values().keys())
        machines = [str(k[1]) for k in keys]
        jobs = [str(k[0]) for k in keys]

        start_jobs = [v() for v in self.model.x.values()]
        start_jobs = pd.to_datetime(self.start_time) + pd.to_timedelta(
            start_jobs, unit=self.time_unit
        )

        durations = pd.to_timedelta(
            [float(self.model.p[k[0], k[1]]) for k in keys], unit=self.time_unit
        )

        end_jobs = start_jobs + durations

        df_out = pd.DataFrame(
            {
                "Tarefa": jobs,
                "Máquina": machines,
                "Início": start_jobs,
                "Duração": durations,
                "Término": end_jobs,
            }
        )

        return df_out.sort_values(by=["Tarefa", "Início"])
