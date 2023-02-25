
import streamlit as st
import pandas as pd
import sqlite3


conn = sqlite3.connect('data.db')
c = conn.cursor()

def  create_usertable ():
    c.execute('CREATE TABLE IF NOT EXISTS usertable(username TEXT,password TEXT)')

def add_userdata(username,password):
    c.execute('INSERT INTO usertable(username,password)VALUES (?,?)',(username,password))
    conn.commit()
def login_user(username,password):
    c.execute('SELECT * FROM usertable WHERE username =? AND password=?',(username,password))
    data=c.fetchall()
    return  data
def view_all_users():
    c.execute('SELECT * FROM usertable')
    data=c.fetchall()
    return data




def main ():
    st.title("Authentification")
    menu=["Accueil","login","inscription"]
    choix=st.sidebar.selectbox("Menu",menu)

    if choix=="home":
        st.subheader("home")

    elif choix=="login":
        st.subheader("section login ")
        username=st.sidebar.text_input("User Name")
        password=st.sidebar.text_input("Password",type='password')
    if st.sidebar.checkbox("login"):
        #if password == '12345':
        create_usertable()
        result = login_user(username,password)
        if result:
            st.success("logged IN as {}".format(username))

            task = st.selectbox("Task", ["Add post", "Analytics", "Profiles"])
            if task == "Add post":
                st.subheader("Add your post")
            elif task == "Analytics":
                st.subheader("Analytics")
            elif task == "Profiles":
                st.subheader("user profiles")
                user_result = view_all_users()
                clean_db = pd.DataFrame(user_result, columns=["Username", "Password"])
                st.dataframe(clean_db)



        else:
            st.warning("password/username Incorrect")



    elif choix=="inscription":

        st.subheader("creer un nv compte")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password",type='password')

        if st.button("inscription"):
            create_usertable()
            add_userdata(new_user,new_password)
            st.success("succssfully")
            st.info("GO to logun Menu to login")

if __name__ == '__main__':
  main()

