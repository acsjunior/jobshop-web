import streamlit as st
from streamlit_option_menu import option_menu

from optplann._pages.about import about_page
from optplann._pages.jobshop import jobshop_page
from optplann._pages.jobshop_formulation import jobshop_formulation_page
from optplann.config.params import PAGES
from optplann.utils import show_page, update_session

st.set_page_config(layout="wide")

page_ids = list(PAGES.keys())
page_titles = [PAGES[key] for key in page_ids]
with st.sidebar:
    selected_item = option_menu(
        "OptPlann",
        page_titles,
        icons=["house", "calculator", "journal-x"],
        menu_icon="cast",
        default_index=0,
    )

page_id = [key for key in PAGES if PAGES[key] == selected_item][0]
session = st.session_state
update_session(session, page_id)

pages = {
    page_ids[0]: lambda x: about_page(x),
    page_ids[1]: lambda x: jobshop_page(x),
    page_ids[2]: lambda x: jobshop_formulation_page(x),
}

show_page(page_id, pages, session)
