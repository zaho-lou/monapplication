import streamlit as st
import pandas as pd
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
def authenticate_user():
    """
    Fonction pour l'authentification de l'utilisateur via Google OAuth2.
    """
    creds = None

    # Vérifiez si les informations d'identification existent déjà dans la session.
    if st.session_state.get("creds", None):
        creds = Credentials.from_authorized_user_info(st.session_state["creds"])

    # Si les informations d'identification n'existent pas, demandez à l'utilisateur de s'authentifier.
    if not creds or not creds.valid:
        st.write("Veuillez vous connecter pour continuer.")
        flow = InstalledAppFlow.from_client_secrets_file(
            "client_secret.json",
            ["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email"],
        )
        creds = flow.run_local_server(port=0)
        st.session_state["creds"] = creds.to_authorized_user_info()

    return creds


def main():
    st.set_page_config(page_title="Mon application Streamlit")

    creds = authenticate_user()

    if creds:
        st.write(f"Bienvenue, {creds.id_token['name']}!")
        st.write(f"Email: {creds.id_token['email']}")
    else:
        st.write("Impossible de vous authentifier.")

if __name__ == "__main__":
    main()


    def main():
        st.set_page_config(page_title="Mon application Streamlit")

        creds = authenticate_user()

        if creds:
            st.write(f"Bienvenue, {creds.id_token['name']}!")
            st.write(f"Email: {creds.id_token['email']}")
        else:
            st.write("Impossible de vous authentifier.")


    if __name__ == "__main__":
        main()







