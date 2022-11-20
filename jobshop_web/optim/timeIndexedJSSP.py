"""
Job Shop Web: a didactic software to solve the job shop scheduling problem with makespan minimization.
Copyright (C) 2022  António C. da Silva Júnior <juniorssz@gmail.com>

This file is part of Job Shop Web.

Job Shop Web is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Job Shop Web is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Job Shop Web.  If not, see <https://www.gnu.org/licenses/>.
"""
import numpy as np
import pandas as pd
import pyomo.environ as pyo

from jobshop_web.optim.model_base import ModelBase


class TimeIndexedJSSP(ModelBase):
    def generate_model(self) -> pyo.ConcreteModel:
        m = len(self.times[0])
        n = len(self.times)
        S = np.sum(np.sum(self.times))

        model = pyo.ConcreteModel()

        # Conjuntos e parâmetros:
        model.J = pyo.RangeSet(n)
        model.M = pyo.RangeSet(m)
        model.H = pyo.RangeSet(0, S, 1)
        model.p = pyo.Param(
            model.J, model.M, initialize=lambda model, j, i: self.times[j - 1][i - 1]
        )
        model.s = pyo.Param(
            model.J, model.M, initialize=lambda model, j, i: self.routes[j - 1][i - 1]
        )

        # Variáveis de decisão:
        model.Cmax = pyo.Var()
        model.y = pyo.Var(model.M, model.J, model.H, within=pyo.Binary)

        # Função objetivo:
        def obj_rule(model):
            return model.Cmax

        model.obj = pyo.Objective(rule=obj_rule, sense=pyo.minimize)

        def constr1_rule(model, i, j):
            return sum(model.y[i, j, t] for t in model.H) == 1

        model.constr1 = pyo.Constraint(model.M, model.J, rule=constr1_rule)

        def constr2_rule(model, i, j):
            return (
                sum((t + model.p[j, i]) * model.y[i, j, t] for t in model.H)
                <= model.Cmax
            )

        model.constr2 = pyo.Constraint(model.M, model.J, rule=constr2_rule)

        def constr_3_rule(model, i, t):
            return (
                sum(
                    model.y[i, j, t_]
                    for j in model.J
                    for t_ in pyo.RangeSet(max(0, t - model.p[j, i] + 1), t, 1)
                )
                <= 1
            )

        model.constr3 = pyo.Constraint(model.M, model.H, rule=constr_3_rule)

        def constr4_rule(model, i, j):
            s_ji = model.s[j, i]
            s_ji1 = model.s[j, i - 1]
            return sum(
                (t + model.p[j, s_ji1]) * model.y[s_ji1, j, t] for t in model.H
            ) <= sum(t * model.y[s_ji, j, t] for t in model.H)

        model.constr4 = pyo.Constraint(
            [i for i in model.M if i >= 2], model.J, rule=constr4_rule
        )

        self.model = model

    def get_output_data(self):
        keys = list(self.model.y.get_values().keys())

        machines = []
        jobs = []
        times = []
        durations = []
        for key in keys:
            j = key[0]
            i = key[1]
            t = key[2]
            d = self.model.p[i, j]
            if self.model.y[j, i, t]():
                machines.append(j)
                jobs.append(i)
                times.append(t)
                durations.append(d)

        df_out = pd.DataFrame(
            {
                "Job": [str(j) for j in jobs],
                "Machine": [str(m) for m in machines],
                "Start": [t for t in times],
                "Duration": durations,
            }
        )

        df_out["Start"] = pd.to_datetime(self.start_time) + pd.to_timedelta(
            df_out["Start"], unit=self.time_unit
        )
        df_out["Duration"] = pd.to_timedelta(df_out["Duration"], unit=self.time_unit)
        df_out["End"] = df_out["Start"] + df_out["Duration"]

        return df_out.sort_values(by=["Job", "Start"])
