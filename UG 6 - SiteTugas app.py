import streamlit as st
from login import login
from data import get_data_tugas
from tugas import tampilkan_tugas, tambah_tugas, edit_tugas

# STEP 1: Buat session state untuk login
if "login" not in st.session_state:
    # TODO: tentukan nilai awal login
    st.session_state.login = False

# STEP 2: Simpan data tugas ke session state
if "tugas" not in st.session_state:
    st.session_state.tugas = get_data_tugas()

# STEP 3: Tampilkan halaman login jika belum login
if not st.session_state.login:
    login()
else:
    st.sidebar.title("📚 Site Tugas")
    st.sidebar.write("Role:", st.session_state.role)

    menu = st.sidebar.radio("Menu", ["Daftar Tugas"])

    # STEP 4: Buat fitur logout
    if st.sidebar.button("Logout"):
        # TODO: reset status login dan role
        st.session_state.login = False
        st.session_state.role = None
        st.rerun()

    if menu == "Daftar Tugas":
        tampilkan_tugas()

        # STEP 5: Fitur tambah dan edit hanya untuk dosen
        if st.session_state.role == "dosen":
            st.write("---")
            tambah_tugas()
            st.write("---")
            edit_tugas()
