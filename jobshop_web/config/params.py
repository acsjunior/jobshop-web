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
PAGES = {
    "about": "Sobre",
    "disjunctiveJSSP": "Modelo disjuntivo (Manne)",
    "disjunctiveJSSP2": "Modelo disjuntivo (Liao)",
    "timeIndexedJSSP": "Modelo indexado no tempo",
    "rankBasedJSSP": "Modelo baseado na ordem",
}

TEMPLATE_TIMES = [[5, 7, 10], [9, 5, 3], [5, 8, 2], [2, 7, 4], [8, 8, 8]]
TEMPLATE_ROUTES = [[2, 1, 3], [1, 2, 3], [3, 2, 1], [2, 1, 3], [3, 1, 2]]

AGGRID_THEME = "alpine"
# AGGRID_THEME = 'streamlit'

TIME_UNITS = {"Minuto": "m", "Hora": "h", "Dia": "D"}

JOB_COL = "Tarefa"
MACHINE_PREFIX = "Máquina"
STAGE_PREFIX = "Etapa"
