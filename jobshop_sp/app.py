import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

from jobshop_sp._pages.about import about_page
from jobshop_sp._pages.disjunctiveJSSP import disjunctiveJSSP_page
from jobshop_sp._pages.disjunctiveJSSP2 import disjunctiveJSSP2_page
from jobshop_sp.config.params import PAGES
from jobshop_sp.config.paths import PATH_ROOT
from jobshop_sp.utils import show_page, update_session

st.set_page_config(
    layout="wide",
    page_title="JSSP",
    page_icon=Image.open(PATH_ROOT / "favicon.ico"),
)


page_ids = list(PAGES.keys())
page_titles = [PAGES[key] for key in page_ids]

with st.sidebar:
    selected_item = option_menu(
        "Job Shop Scheduling Problem",
        page_titles,
        icons=["house", "calculator", "calculator"],
        menu_icon="cast",
        default_index=0,
    )

page_id = [key for key in PAGES if PAGES[key] == selected_item][0]
session = st.session_state
update_session(session, page_id)

pages = {
    page_ids[0]: lambda x: about_page(x),
    page_ids[1]: lambda x: disjunctiveJSSP_page(x),
    page_ids[2]: lambda x: disjunctiveJSSP2_page(x),
}

show_page(page_id, pages, session)
