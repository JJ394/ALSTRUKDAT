import streamlit as st

def tampilkan_tugas():
    st.header("📋 Daftar Tugas")

    search = st.text_input("🔍 Cari tugas")
    urutan = st.selectbox("Urutkan", ["Default", "Ascending", "Descending"])
    data = st.session_state.tugas.copy()

    # STEP 1: Filter tugas berdasarkan search
    if search:
        # TODO: cari berdasarkan judul atau mata kuliah
        data = [
            tugas for tugas in data 
            if search.lower() in tugas["judul"].lower() or search.lower() in tugas["mata_kuliah"].lower()
        ]

    # STEP 2: Urutkan berdasarkan deadline
    if urutan == "Ascending":
        # TODO: sorting dari deadline terkecil
        for i in data:
            data = sorted(data, key=lambda x: x["deadline"])
    elif urutan == "Descending":
        # TODO: sorting dari deadline terbesar
        for i in data:
            data = sorted(data, key=lambda x: x["deadline"], reverse=True)

    if len(data) == 0:
        st.warning("Tugas tidak ditemukan.")
    else:
        for tugas in data:
            st.write("---")
            col1, col2 = st.columns([4, 1])

            with col1:
                st.subheader(tugas["judul"])
                st.write("Mata Kuliah:", tugas["mata_kuliah"])
                st.write("Deadline:", tugas["deadline"])

            with col2:
                if st.session_state.role == "dosen":
                    if st.button("Edit", key="edit_" + str(tugas["id"])):
                        # STEP 3: Simpan ID tugas yang akan diedit
                        st.session_state["edit_id"] = tugas["id"]
                        st.rerun()


def tambah_tugas():
    st.header("➕ Tambah Tugas")

    judul = st.text_input("Judul Tugas")
    mata_kuliah = st.text_input("Mata Kuliah")
    deadline = st.date_input("Deadline")

    if st.button("Tambah"):
        if judul and mata_kuliah:
            id_baru = len(st.session_state.tugas) + 1

            tugas_baru = {
                "id": id_baru,
                "judul": judul,
                "mata_kuliah": mata_kuliah,
                "deadline": str(deadline)
            }

            # STEP 4: Tambahkan tugas baru ke data
            if 'tugas_baru' not in st.session_state:
                st.session_state.tugas.append(tugas_baru)

            st.success("Tugas berhasil ditambahkan!")
        else:
            st.warning("Semua data harus diisi.")


def edit_tugas():
    if "edit_id" not in st.session_state:
        return

    tugas_edit = None

    for tugas in st.session_state.tugas:
        if tugas["id"] == st.session_state.edit_id:
            tugas_edit = tugas

    if tugas_edit is None:
        return

    st.header("✏️ Edit Tugas")

    judul = st.text_input("Judul Tugas", value=tugas_edit["judul"])
    mata_kuliah = st.text_input("Mata Kuliah", value=tugas_edit["mata_kuliah"])
    deadline = st.text_input("Deadline", value=tugas_edit["deadline"])

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Simpan Perubahan"):
            # STEP 5: Update data tugas
            tugas_edit["judul"] = judul
            tugas_edit["mata_kuliah"] = mata_kuliah
            tugas_edit["deadline"] = deadline

            # STEP 6: Hapus edit_id setelah disimpan
            del st.session_state["edit_id"]

            st.success("Tugas berhasil diubah!")
            st.rerun()

    with col2:
        if st.button("Batal"):
            # STEP 7: Batalkan proses edit
            del st.session_state["edit_id"]
            st.rerun()
