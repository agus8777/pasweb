import streamlit as st

# Pengaturan Dasar Halaman
st.set_page_config(page_title="Team Insurance Landing Page", layout="wide")

# Database Sederhana (Dalam memori, untuk contoh)
if 'content' not in st.session_state:
    st.session_state['content'] = {
        'title': "Perlindungan Masa Depan Keluarga Anda",
        'sub_title': "Kami membantu Anda merencanakan masa depan yang lebih tenang.",
        'description': "Tim agen profesional kami siap membantu kebutuhan asuransi Anda.",
    }

# --- SIDEBAR: LOGIN ADMIN ---
st.sidebar.title("Admin Panel")
password = st.sidebar.text_input("Masukkan Password Admin", type="password")

# Cek Password (Ganti 'rahasia123' dengan password pilihan Anda)
is_admin = (password == "rahasia123")

if is_admin:
    st.sidebar.success("Mode Edit Aktif")
    st.sidebar.markdown("---")
    
    # Form Edit Konten
    new_title = st.sidebar.text_input("Edit Judul Utama", st.session_state['content']['title'])
    new_sub = st.sidebar.text_area("Edit Sub-judul", st.session_state['content']['sub_title'])
    new_desc = st.sidebar.text_area("Edit Deskripsi", st.session_state['content']['description'])
    
    if st.sidebar.button("Simpan Perubahan"):
        st.session_state['content']['title'] = new_title
        st.session_state['content']['sub_title'] = new_sub
        st.session_state['content']['description'] = new_desc
        st.rerun()
else:
    if password:
        st.sidebar.error("Password Salah")

# --- HALAMAN UTAMA (LANDING PAGE) ---
st.title(st.session_state['content']['title'])
st.subheader(st.session_state['content']['sub_title'])
st.write(st.session_state['content']['description'])

st.divider()

# Bagian Tim
col1, col2 = st.columns(2)
with col1:
    st.image("https://via.placeholder.com/400x300", caption="Foto Tim Anda")
with col2:
    st.markdown("""
    ### Mengapa Memilih Tim Kami?
    * Pengalaman terpercaya bertahun-tahun.
    * Klaim yang dibantu hingga tuntas.
    * Konsultasi gratis untuk perencanaan warisan dan kesehatan.
    """)

# Tombol Kontak
st.link_button("Hubungi Kami via WhatsApp", "https://wa.me/628123456789")