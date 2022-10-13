import streamlit as st

from jobshop_sp._pages.utils import get_formulation


def disjunctiveJSSP_formulation_page(session):
    st.markdown(get_formulation(session))
