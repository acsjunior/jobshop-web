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
import streamlit as st
from st_aggrid import AgGrid

import jobshop_web._pages.utils as page
from jobshop_web.config.params import (AGGRID_THEME, JOB_COL, MACHINE_PREFIX,
                                       STAGE_PREFIX, TIME_UNITS)
from jobshop_web.optim.timeIndexedJSSP import TimeIndexedJSSP

MODEL_CLASS = TimeIndexedJSSP


def timeIndexedJSSP_page(session):
    st.header(page.get_title(session))
    st.markdown("---")

    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            n_jobs = st.number_input(label="Número de tarefas", min_value=1, value=4)
        with col2:
            n_machines = st.number_input(
                label="Número de máquinas", min_value=1, value=3
            )
        with col3:
            dt_start = st.date_input("Data de início")
        with col4:
            hr_start = st.time_input("Horário de início")
        with col5:
            time_unit = st.selectbox("Unidade de tempo", tuple(TIME_UNITS.keys()))

        col1, col2, col3 = st.columns([1, 3, 1])
        with col1:
            is_import_csv_selected = (
                st.radio("Dados de entrada", ["Digitar", "Importar CSV"])
                == "Importar CSV"
            )
        with col2:
            if is_import_csv_selected:
                uploaded_tp = st.file_uploader(
                    "Carregar tempos de processamento", type=["csv"]
                )
                uploaded_rp = st.file_uploader(
                    "Carregar rotas de processamento", type=["csv"]
                )

        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
        with col2:
            if is_import_csv_selected:
                page.show_btn_download_csv(
                    page.get_template_times(),
                    label="Baixar template tempos",
                    filename="template_tempos.csv",
                )
        with col3:
            if is_import_csv_selected:
                page.show_btn_download_csv(
                    page.get_template_routes(),
                    label="Baixar template rotas",
                    filename="template_rotas.csv",
                )

        if (
            is_import_csv_selected
            and uploaded_tp is not None
            and uploaded_rp is not None
        ):
            df_tp = page.convert_uploaded_df_to_grid(
                pd.read_csv(uploaded_tp), JOB_COL, MACHINE_PREFIX
            )
            df_rp = page.convert_uploaded_df_to_grid(
                pd.read_csv(uploaded_rp), JOB_COL, STAGE_PREFIX
            )
        else:
            df_tp = page.get_input_df(
                n_jobs, n_machines, first_col=JOB_COL, prefix=MACHINE_PREFIX
            )
            df_rp = page.get_input_df(
                n_jobs, n_machines, first_col=JOB_COL, prefix=STAGE_PREFIX
            )

        st.subheader("Tempos de processamento")
        df_tp = page.generate_input_grid(df_tp)["data"]

        st.subheader("Rotas de processamento")
        df_rp = page.generate_input_grid(df_rp)["data"]

        ##### Resolução do problema #####
        col1, col2, col3, col4, col5 = st.columns(5)
        with col3:
            btn_solve = st.button("Resolver")

        if btn_solve:
            df_tp, tp_is_valid, tp_log_msgs = page.validate_input_grid(df_tp, JOB_COL)
            if tp_is_valid:
                df_rp, rp_is_valid, rp_log_msgs = page.validate_input_grid(
                    df_rp, JOB_COL
                )
                if not rp_is_valid:
                    for msg in rp_log_msgs:
                        st.error(msg)
            else:
                for msg in tp_log_msgs:
                    st.error(msg)

            if tp_is_valid and rp_is_valid:

                # Resolve o modelo:
                tempos = page.get_array(df_tp, JOB_COL)
                rotas = page.get_array(df_rp, JOB_COL)
                start_time = pd.to_datetime(f"{dt_start} {hr_start}")
                model = MODEL_CLASS(tempos, rotas, start_time, TIME_UNITS[time_unit])
                model.solve()

                page.show_solver_log(
                    model.is_optimal, model.solver_time, model.objective
                )

                # Visualização dos dados de saída:
                df_out = model.get_output_data()
                st.plotly_chart(page.get_gantt(df_out), use_container_width=True)
                output_grid = page.generate_output_grid(df_out)

                col1, col2, col3, col4, col5 = st.columns(5)
                with col3:
                    page.show_btn_download_results(df_out)
