"""
Job Shop Web: a didactic software to solve the job shop scheduling problem with makespan minimization.
Copyright (C) 2022  António C. da Silva Júnior <juniorssz@gmail.com>

This file is part of Job Shop Web.

Job Shop Web is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Job Shop Web is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Job Shop Web.  If not, see <https://www.gnu.org/licenses/>.
"""
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
