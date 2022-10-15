import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder

from jobshop_sp.config.params import (AGGRID_THEME, PAGES, TEMPLATE_ROUTES,
                                      TEMPLATE_TIMES)
from jobshop_sp.config.paths import PATH_FORMULATIONS


def get_title(session):
    return PAGES[session["page"]]


def get_key(session, prefix):
    return f"{prefix}_{session['page']}"


def get_formulation(session):
    prefix = session["page"].split("_")[0]
    with open(PATH_FORMULATIONS / f"{prefix}.md") as f:
        return f.read()


def get_input_df(n_rows: int, n_cols: int, first_col: str, prefix: str):
    dict_df = {}
    dict_df[first_col] = [str(j + 1) for j in range(n_rows)]
    for col in range(n_cols):
        dict_df[f"{prefix} {col+1}"] = [0 for j in range(n_rows)]

    return pd.DataFrame(dict_df)


def get_array(df, col_to_drop):
    return np.array(df.drop(columns=col_to_drop))


def show_btn_download_csv(df: pd.DataFrame, label: str, filename: str):
    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label=label,
        data=csv,
        file_name=filename,
        mime="text/csv",
    )


def convert_uploaded_df_to_grid(df: pd.DataFrame, first_col, prefix) -> pd.DataFrame:
    df.columns = [f"{prefix} {str(j+1)}" for j in range(len(df.columns))]
    df[first_col] = [i + 1 for i in range(len(df.index))]
    sorted_columns = [first_col] + [col for col in df.columns if col != first_col]
    return df[sorted_columns]


def validate_input_grid(df: pd.DataFrame, first_col: str):
    log_msgs = []
    is_valid = True
    for col in df.columns:
        if col == first_col:
            df[col] = df[col].astype(str)
        else:
            try:
                df[col] = df[col].astype(float)
                n_nans = df[col].isna().sum()
                if n_nans > 0:
                    log_msgs.append(f"Dado(s) incorreto(s) na coluna {col}")
                    is_valid = False
                if df[df[col] == 0].shape[0] > 0:
                    log_msgs.append(f"Células zeradas na coluna {col}")
                    is_valid = False
            except:
                log_msgs.append(f"Dado(s) incorreto(s) na coluna {col}")
                is_valid = False

    return df, is_valid, log_msgs


def generate_input_grid(df: pd.DataFrame):
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(
        sorteable=False,
        filterable=False,
        resizable=False,
        groupable=False,
        editable=True,
        width=130,
        type="f",
    )
    first_col = df.columns[0]
    gb.configure_column(first_col, editable=False, width=80)

    go = gb.build()

    return AgGrid(
        df, gridOptions=go, enable_enterprise_modules=False, theme=AGGRID_THEME
    )


def show_solver_log(is_optimal: bool, solver_time: float, objective: float):
    if is_optimal:
        st.success(
            f"""
            Solução ótima encontrada em {np.round(solver_time,4)} segundos. \n
            Função objetivo {objective}.
            """
        )
    else:
        st.error("Não foi possível encontrar uma solução factível.")


def get_gantt(df: pd.DataFrame):
    fig = px.timeline(
        df,
        x_start="Início",
        x_end="Término",
        y="Máquina",
        color="Tarefa",
        title="Gráfico de Gantt",
    )

    fig.update_yaxes(autorange="reversed")

    return fig


def show_btn_download_results(df: pd.DataFrame):
    st.download_button(
        label="Baixar plano",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name=f"results.csv",
        mime="text/csv",
    )


def get_template_times() -> pd.DataFrame:
    data = np.array(TEMPLATE_TIMES)
    df = pd.DataFrame(data)
    df.columns = ["machine1", "machine2", "machine3"]
    return df


def get_template_routes() -> pd.DataFrame:
    data = np.array(TEMPLATE_ROUTES)
    df = pd.DataFrame(data)
    df.columns = ["step1", "step2", "step3"]
    return df
