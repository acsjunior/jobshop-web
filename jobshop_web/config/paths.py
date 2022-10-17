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
from pathlib import Path

PATH_ROOT = Path(__file__).parents[1].absolute()

PATH_FORMULATIONS = PATH_ROOT / "formulations"
