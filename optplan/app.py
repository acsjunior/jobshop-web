import streamlit as st
from streamlit_option_menu import option_menu

from optplan._pages.about import about_page
from optplan._pages.jobshop import jobshop_page
from optplan.config.params import PAGE_TITLES
from optplan.utils import clean_session, show_screen, update_session

st.set_page_config(layout="wide")

with st.sidebar:
    screen = option_menu(
        "OptPlan",
        PAGE_TITLES,
        icons=["house", "calculator"],
        menu_icon="cast",
        default_index=0,
    )

session = st.session_state
update_session(session, screen)
clean_session(session)

screens = {
    PAGE_TITLES[0]: lambda x: about_page(x),
    PAGE_TITLES[1]: lambda x: jobshop_page(x),
}

show_screen(screen, screens, session)
