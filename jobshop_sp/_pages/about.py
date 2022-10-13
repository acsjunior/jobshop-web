import streamlit as st

from jobshop_sp._pages.utils import get_title


def about_page(session):
    st.header(get_title(session))
