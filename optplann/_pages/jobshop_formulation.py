from ctypes import util

import streamlit as st

from optplann._pages.utils import get_formulation, get_title


def jobshop_formulation_page(session):
    st.markdown(get_formulation(session))