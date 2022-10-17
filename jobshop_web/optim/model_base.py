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
from abc import ABC, abstractmethod

import numpy as np
import pandas as pd
import pyomo.environ as pyo


class IModel(ABC):
    @property
    @abstractmethod
    def name(self) -> pyo.ConcreteModel:
        pass

    @property
    @abstractmethod
    def times(self) -> np.array:
        pass

    @property
    @abstractmethod
    def routes(self) -> np.array:
        pass

    @property
    @abstractmethod
    def start_time(self) -> pd.Timestamp:
        pass

    @property
    @abstractmethod
    def time_unit(self) -> str:
        pass

    @property
    @abstractmethod
    def solver_time(self) -> float:
        pass

    @property
    @abstractmethod
    def objective(self) -> float:
        pass

    @property
    @abstractmethod
    def is_optimal(self) -> bool:
        pass

    @abstractmethod
    def generate_model(self):
        pass

    @abstractmethod
    def solve(self, solver: str):
        pass

    @abstractmethod
    def get_output_data(self) -> pd.DataFrame:
        pass

    @abstractmethod
    def get_solver_data(self, result) -> pd.DataFrame:
        pass


class ModelBase(IModel):
    def name(self) -> pyo.ConcreteModel:
        return super().name

    def times(self) -> np.array:
        return super().times

    def routes(self) -> np.array:
        return super().routes

    def start_time(self) -> pd.Timestamp:
        return super().start_time

    def time_unit(self) -> str:
        return super().time_unit

    def solver_time(self) -> float:
        return super().solver_time

    def objective(self) -> float:
        return super().objective

    def is_optimal(self) -> bool:
        return super().is_optimal

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

        self.generate_model()

    def generate_model(self):
        return super().generate_model()

    def solve(self, solver: str = "glpk"):
        result = pyo.SolverFactory(solver).solve(self.model)
        self.get_solver_data(result)

    def get_output_data(self) -> pd.DataFrame:
        return super().get_output_data()

    def get_solver_data(self, result) -> pd.DataFrame:
        self.solver_time = result["Solver"][0]["Time"]
        self.is_optimal = (
            result["Solver"][0]["Termination condition"].value == "optimal"
        )
        if self.is_optimal:
            self.objective = result["Problem"][0]["Lower bound"]
