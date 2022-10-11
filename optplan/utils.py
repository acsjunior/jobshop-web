def show_screen(screen, screens, session):
    screens[screen](session)


def update_session(session, screen):
    if "screen" not in session:
        session["screen"] = screen
        session["previous_screen"] = screen
    else:
        session["previous_screen"] = session["screen"]
        session["screen"] = screen


def clean_session(session):
    if session["screen"] != session["previous_screen"]:
        keys_to_remove = [
            key
            for key in session.keys()
            if key.startswith(f"model_{session['previous_screen']}")
        ]
        if len(keys_to_remove) > 0:
            for key in keys_to_remove:
                del session[key]
