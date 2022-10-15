import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

from jobshop_web._pages.about import about_page
from jobshop_web._pages.disjunctiveJSSP import disjunctiveJSSP_page
from jobshop_web._pages.disjunctiveJSSP2 import disjunctiveJSSP2_page
from jobshop_web._pages.rankBasedJSSP import rankBasedJSSP_page
from jobshop_web._pages.timeIndexedJSSP import timeIndexedJSSP_page
from jobshop_web.config.params import PAGES
from jobshop_web.config.paths import PATH_ROOT
from jobshop_web.utils import hide_hamburger_menu, show_page, update_session

st.set_page_config(
    layout="wide",
    page_title="Job Shop Web",
    page_icon=Image.open(PATH_ROOT / "favicon.ico"),
)

hide_hamburger_menu()

page_ids = list(PAGES.keys())
page_titles = [PAGES[key] for key in page_ids]

with st.sidebar:
    selected_item = option_menu(
        "Job Shop Web",
        page_titles,
        icons=["house", "calculator", "calculator", "calculator", "calculator"],
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
    page_ids[3]: lambda x: timeIndexedJSSP_page(x),
    page_ids[4]: lambda x: rankBasedJSSP_page(x),
}

show_page(page_id, pages, session)
