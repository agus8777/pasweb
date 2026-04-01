import streamlit as st

# 1. Inisialisasi Database Sederhana
if 'db' not in st.session_state:
    st.session_state['db'] = {
        'password': "admin123",
        'secret_key': "PAS-2026",
        'title': "Pru Agus Sophie (PAS) Team",
        'agent_name': "Agus Sophie",
        'position': "Senior Business Director",
        'sub_title': "Perencanaan Keuangan Masa Depan yang Cerdas & Aman",
        'wa_number': "628123456789",
        'img_url': "https://drive.google.com/file/d/1J-DQGIH3-JLzG-nr9GuH5PE97TukVrSY/view?usp=sharing",
        'markdown_content': """
### Mengapa Memilih Tim Kami?
* **Pengalaman Terpercaya:** Melayani nasabah dengan integritas tinggi.
* **Pendampingan Klaim:** Kami bantu proses klaim hingga tuntas.
* **Edukasi Finansial:** Konsultasi gratis untuk perencanaan warisan dan kesehatan.
        """
    }

# Status Login
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

st.set_page_config(page_title=st.session_state['db']['title'], layout="wide")

# --- FUNGSI RESET PASSWORD ---
def reset_password_ui():
    st.divider()
    st.subheader("🔑 Reset Password")
    sk_input = st.text_input("Masukkan Kunci Rahasia", type="password")
    new_pw = st.text_input("Password Baru")
    if st.button("Update Password"):
        if sk_input == st.session_state['db']['secret_key']:
            st.session_state['db']['password'] = new_pw
            st.success("Berhasil! Silakan login di sidebar.")
        else:
            st.error("Kunci Rahasia salah.")

# --- SIDEBAR: ADMIN PANEL ---
st.sidebar.title("🔐 Admin Panel")

if not st.session_state['logged_in']:
    input_pw = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if input_pw == st.session_state['db']['password']:
            st.session_state['logged_in'] = True
            st.rerun()
        else:
            st.sidebar.error("Password Salah")
    
    if st.sidebar.button("Lupa Password?"):
        st.session_state['show_reset'] = True
else:
    st.sidebar.success(f"Halo, {st.session_state['db']['agent_name']}")
    if st.sidebar.button("Logout / Keluar"):
        st.session_state['logged_in'] = False
        st.rerun()

    st.sidebar.markdown("---")
    with st.sidebar.expander("📝 Edit Konten Website", expanded=True):
        st.session_state['db']['title'] = st.text_input("Judul Web", st.session_state['db']['title'])
        st.session_state['db']['agent_name'] = st.text_input("Nama Agen", st.session_state['db']['agent_name'])
        st.session_state['db']['position'] = st.text_input("Jabatan", st.session_state['db']['position'])
        st.session_state['db']['sub_title'] = st.text_area("Sub-Judul", st.session_state['db']['sub_title'])
        st.session_state['db']['wa_number'] = st.text_input("No WhatsApp (62...)", st.session_state['db']['wa_number'])
        st.session_state['db']['img_url'] = st.text_input("Link Foto Google Drive", st.session_state['db']['img_url'])
        st.session_state['db']['markdown_content'] = st.text_area("Isi Markdown (Poin-poin)", st.session_state['db']['markdown_content'], height=200)
        
        if st.button("Simpan Perubahan"):
            st.toast("Perubahan Berhasil Disimpan!")
            st.rerun()

# --- TAMPILAN UTAMA (LANDING PAGE) ---
if st.session_state.get('show_reset') and not st.session_state['logged_in']:
    reset_password_ui()
    if st.button("Kembali"):
        del st.session_state['show_reset']
        st.rerun()
else:
    # Header Section
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.title(st.session_state['db']['title'])
        st.subheader(f"{st.session_state['db']['agent_name']} - {st.session_state['db']['position']}")
        st.write(st.session_state['db']['sub_title'])
        st.link_button("Konsultasi via WhatsApp", f"https://wa.me/{st.session_state['db']['wa_number']}")
    
    with col2:
        try:
            url_foto = st.session_state['db']['img_url']
            # Deteksi Otomatis Format Link Google Drive
            if "drive.google.com" in url_foto:
                if "/file/d/" in url_foto:
                    file_id = url_foto.split("/file/d/")[1].split("/")[0]
                elif "id=" in url_foto:
                    file_id = url_foto.split("id=")[1].split("&")[0]
                url_foto = f"https://drive.google.com/thumbnail?id={file_id}&sz=w1000"
            
            st.image(url_foto, use_container_width=True)
        except Exception:
            st.image("https://via.placeholder.com/800x600?text=Format+Link+Salah")

    st.divider()
    
    # Bagian Markdown yang bisa diedit
    st.markdown(st.session_state['db']['markdown_content'])
