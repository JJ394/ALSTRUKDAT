import streamlit as st

def login():
    st.title("📚 Site Tugas")
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        # STEP 1: Cek login sebagai murid
        if username == "murid" and password == "123":
            # TODO: simpan status login dan role murid
            st.session_state['login'] = True
            st.session_state['role'] = "murid"
            st.switch_page("app.py")
            st.rerun()

        # STEP 2: Cek login sebagai dosen
        elif username == "dosen" and password == "123":
            # TODO: simpan status login dan role dosen
            st.session_state['login'] = True
            st.session_state['role'] = "dosen"
            st.switch_page("app.py")
            st.rerun()

        else:
            # STEP 3: Tampilkan pesan jika login salah
            st.error("Username atau password salah")
