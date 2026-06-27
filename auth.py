import streamlit_authenticator as stauth

def login():

    names = ["Admin"]
    usernames = ["admin"]
    passwords = ["admin123"]

    hashed_passwords = stauth.Hasher(passwords).generate()

    authenticator = stauth.Authenticate(
        names,
        usernames,
        hashed_passwords,
        "ats_app",
        "abcdef",
        cookie_expiry_days=1
    )

    name, auth_status, username = authenticator.login("Login", "main")

    return name, auth_status, authenticator