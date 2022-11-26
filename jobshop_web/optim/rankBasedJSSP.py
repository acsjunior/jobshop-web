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


class RankBasedJSSP(ModelBase):
    def generate_model(self) -> pyo.ConcreteModel:
        m = len(self.times[0])
        n = len(self.times)
        V = sum(sum(self.times))

        model = pyo.ConcreteModel()

        # Conjuntos e parâmetros:
        model.J = pyo.RangeSet(n)
        model.M = pyo.RangeSet(m)
        model.p = pyo.Param(
            model.J, model.M, initialize=lambda model, j, i: self.times[j - 1][i - 1]
        )
        model.r = pyo.Param(
            model.J,
            model.M,
            model.M,
            initialize=lambda model, j, i, l: 1
            if self.routes[j - 1][l - 1] == i
            else 0,
        )

        # Variáveis de decisão:
        model.Cmax = pyo.Var()
        model.w = pyo.Var(model.J, model.J, model.M, within=pyo.Binary)
        model.h = pyo.Var(model.M, model.J, within=pyo.NonNegativeReals)

        # Função objetivo:
        def obj_rule(model):
            return model.Cmax

        model.obj = pyo.Objective(rule=obj_rule, sense=pyo.minimize)

        def constr1_rule(model, k, i):
            return sum(model.w[j, k, i] for j in model.J) == 1

        model.constr1 = pyo.Constraint(model.J, model.M, rule=constr1_rule)

        def constr2_rule(model, j, i):
            return sum(model.w[j, k, i] for k in model.J) == 1

        model.constr2 = pyo.Constraint(model.J, model.M, rule=constr2_rule)

        def constr3_rule(model, k, i):
            return (
                model.h[i, k] + sum(model.p[j, i] * model.w[j, k, i] for j in model.J)
                <= model.h[i, k + 1]
            )

        model.constr3 = pyo.Constraint(
            [k for k in model.J if k < n], model.M, rule=constr3_rule
        )

        def constr4_rule(model, j, k, k_, l):
            a = sum(model.r[j, i, l] * model.h[i, k] for i in model.M)
            b = sum(model.r[j, i, l] * model.p[j, i] for i in model.M)
            c = V * (1 - sum(model.r[j, i, l] * model.w[j, k, i] for i in model.M))
            d = V * (1 - sum(model.r[j, i, l + 1] * model.w[j, k_, i] for i in model.M))
            e = sum(model.r[j, i, l + 1] * model.h[i, k_] for i in model.M)
            return a + b <= c + d + e

        model.constr4 = pyo.Constraint(
            model.J, model.J, model.J, [l for l in model.M if l < m], rule=constr4_rule
        )

        def constr5_rule(model, k, i):
            return (
                model.h[i, n] + sum(model.p[j, i] * model.w[j, n, i] for j in model.J)
                <= model.Cmax
            )

        model.constr5 = pyo.Constraint(model.J, model.M, rule=constr5_rule)

        self.model = model

    def get_output_data(self):
        keys = [
            key for key in self.model.w if self.model.w[key[0], key[1], key[2]]() == 1.0
        ]

        machines = []
        jobs = []
        start_jobs = []
        for key in self.model.h:
            machine = key[0]
            operation = key[1]

            start_job = self.model.h[machine, operation]()
            start_job = pd.to_datetime(self.start_time) + pd.to_timedelta(
                start_job, unit=self.time_unit
            )

            job = list(filter(lambda x: x[2] == machine and x[1] == operation, keys))[
                0
            ][0]

            machines.append(str(machine))
            jobs.append(str(job))
            start_jobs.append(start_job)

        df_out = pd.DataFrame(
            {"Job": jobs, "Machine": machines, "Start": start_jobs}
        )
        df_out = df_out.sort_values(by=["Job", "Start"]).reset_index(drop=True)
        df_out["route"] = (df_out.groupby("Job")["Start"].rank()).astype(int)

        durations = pd.to_timedelta(
            df_out.apply(
                lambda x: self.model.p[int(x["Job"]), int(x["Machine"])], axis=1
            ),
            unit=self.time_unit,
        )
        df_out["Duration"] = durations

        df_out["End"] = df_out["Start"] + durations

        del df_out["route"]

        return df_out.sort_values(by=["Job", "Start"])
