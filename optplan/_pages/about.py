import streamlit as st

from optplan._pages.utils import get_title


def about_page(session):
    st.header(get_title(session))
