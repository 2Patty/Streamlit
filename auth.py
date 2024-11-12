import streamlit as st
from home import home_page

# Authentication function
def authenticate():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        login_form()
    else:
        show_authenticated_content()

        # Login form function
def login_form():
    st.title("Login")
    username = st.text_input("Username", key="username_input")
    password = st.text_input("Password", type="password", key="password_input")

    if st.button("Login"):
        if username == "admin" and password == "Thegame":  # Simple login check
            st.session_state.authenticated = True
            st.success("Successfully logged in!")
        else:
            st.error("Invalid credentials")

# Show content after successful authentication
def show_authenticated_content():
    st.sidebar.title("Navigation")
    #st.sidebar.button("Home", on_click=home_page)

    # Add a logout button
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.success("Logged out!")

if __name__ == "__main__":
    authenticate()
    
    