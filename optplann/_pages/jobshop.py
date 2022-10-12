import numpy as np
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from optplann._pages.utils import (generate_input_grid, get_array, get_gantt,
                                   get_input_df, get_title,
                                   show_btn_download_results, show_solver_log,
                                   validate_input_grid)
from optplann.config.params import (JOB_COL, MACHINE_PREFIX, STAGE_PREFIX,
                                    TIME_UNITS)
from optplann.optim.jobshop import JobShop


def jobshop_page(session):
    st.header(get_title(session))

    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            n_jobs = st.number_input(label="Número de tarefas", min_value=1, value=3)
        with col2:
            n_machines = st.number_input(
                label="Número de máquinas", min_value=1, value=3
            )
        with col3:
            dt_start = st.date_input("Data de início")
            # btn_update_grids = st.button("Atualizar tabelas")
        with col4:
            hr_start = st.time_input("Horário de início")
        with col5:
            time_unit = st.selectbox("Unidade de tempo", tuple(TIME_UNITS.keys()))

        st.subheader("Tempos de processamento")
        df_tp = get_input_df(
            n_jobs, n_machines, first_col=JOB_COL, prefix=MACHINE_PREFIX
        )
        df_tp = generate_input_grid(df_tp)["data"]

        st.subheader("Rotas de processamento")
        df_rp = get_input_df(n_jobs, n_machines, first_col=JOB_COL, prefix=STAGE_PREFIX)
        df_rp = generate_input_grid(df_rp)["data"]

        ##### Resolução do problema #####
        col1, col2, col3, col4, col5 = st.columns(5)
        with col3:
            btn_solve = st.button("Resolver")

        if btn_solve:
            df_tp, tp_is_valid, tp_log_msgs = validate_input_grid(df_tp, JOB_COL)
            if tp_is_valid:
                df_rp, rp_is_valid, rp_log_msgs = validate_input_grid(df_rp, JOB_COL)
                if not rp_is_valid:
                    for msg in rp_log_msgs:
                        st.error(msg)
            else:
                for msg in tp_log_msgs:
                    st.error(msg)

            if tp_is_valid and rp_is_valid:

                # Resolve o modelo:
                tempos = get_array(df_tp, JOB_COL)
                rotas = get_array(df_rp, JOB_COL)
                start_time = pd.to_datetime(f"{dt_start} {hr_start}")
                jobshop = JobShop(tempos, rotas, start_time, TIME_UNITS[time_unit])
                jobshop.solve()

                show_solver_log(jobshop.is_optimal, jobshop.solver_time)

                df_out = jobshop.get_output_data()
                st.plotly_chart(get_gantt(df_out))

                AgGrid(df_out, height=250, enable_enterprise_modules=False)

                st.info(f"Função objetivo {jobshop.objective}")

                col1, col2, col3, col4, col5 = st.columns(5)
                with col3:
                    show_btn_download_results(df_out)
