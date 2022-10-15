import streamlit as st


def show_page(page, pages, session):
    pages[page](session)


def update_session(session, page):
    if "page" not in session:
        session["page"] = page
        session["previous_page"] = page
    else:
        session["previous_page"] = session["page"]
        session["page"] = page


def hide_hamburger_menu():
    hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
    st.markdown(hide_menu_style, unsafe_allow_html=True)
