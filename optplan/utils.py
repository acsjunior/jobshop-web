def show_page(page, pages, session):
    pages[page](session)


def update_session(session, page):
    if "page" not in session:
        session["page"] = page
        session["previous_page"] = page
    else:
        session["previous_page"] = session["page"]
        session["page"] = page
