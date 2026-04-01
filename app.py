import streamlit as st

# 1. Inisialisasi Data (Database Sederhana)
if 'db' not in st.session_state:
    st.session_state['db'] = {
        'password': "admin123",
        'secret_key': "PAS-2026", # Gunakan ini jika lupa password
        'title': "Pru Agus Sophie (PAS) Team",
        'sub_title': "Perencanaan Keuangan Masa Depan yang Cerdas & Aman",
        'wa_number': "628123456789",
        'img_url': "https://images.unsplash.com/photo-1450101499163-c8848c66ca85", # Foto Default
    }

st.set_page_config(page_title=st.session_state['db']['title'], layout="wide")

# --- FUNGSI RESET PASSWORD ---
def reset_password_ui():
    st.divider()
    st.subheader("Reset Password")
    sk_input = st.text_input("Masukkan Kunci Rahasia Anda", type="password")
    new_pw = st.text_input("Masukkan Password Baru")
    
    if st.button("Update Password"):
        if sk_input == st.session_state['db']['secret_key']:
            st.session_state['db']['password'] = new_pw
            st.success("Password berhasil diganti! Silakan login di sidebar.")
        else:
            st.error("Kunci Rahasia salah.")

# --- SIDEBAR: LOGIN & ADMIN ---
st.sidebar.title("🔐 Admin Panel")
input_pw = st.sidebar.text_input("Password", type="password")

if input_pw == st.session_state['db']['password']:
    st.sidebar.success("Mode Edit Aktif")
    
    with st.sidebar.expander("Ganti Konten Website"):
        new_title = st.text_input("Judul Website", st.session_state['db']['title'])
        new_sub = st.text_area("Sub-Judul", st.session_state['db']['sub_title'])
        new_wa = st.text_input("Nomor WhatsApp (Gunakan 62...)", st.session_state['db']['wa_number'])
        new_img = st.text_input("URL Foto (Google Drive/Lainnya)", st.session_state['db']['img_url'])
        
        if st.button("Simpan Perubahan"):
            st.session_state['db'].update({
                'title': new_title, 'sub_title': new_sub, 
                'wa_number': new_wa, 'img_url': new_img
            })
            st.rerun()
            
else:
    if input_pw:
        st.sidebar.error("Password Salah")
    if st.sidebar.button("Lupa Password?"):
        st.session_state['show_reset'] = True

# --- TAMPILAN UTAMA ---
if st.session_state.get('show_reset'):
    reset_password_ui()
    if st.button("Kembali ke Beranda"):
        del st.session_state['show_reset']
        st.rerun()
else:
    # Header Section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title(st.session_state['db']['title'])
        st.write(st.session_state['db']['sub_title'])
        st.link_button(f"Hubungi Kami (WA)", f"https://wa.me/{st.session_state['db']['wa_number']}")
    
    with col2:
        # --- LOGIKA DETEKSI OTOMATIS LINK GOOGLE DRIVE ---
        try:
            url_foto = st.session_state['db']['img_url']
            
            # Cek apakah ini link Google Drive standar
            if "drive.google.com" in url_foto:
                if "/file/d/" in url_foto:
                    # Mengambil ID di antara /d/ dan /view
                    file_id = url_foto.split("/file/d/")[1].split("/")[0]
                    url_foto = f"https://drive.google.com/thumbnail?id={file_id}&sz=w1000"
                elif "id=" in url_foto:
                    # Mengambil ID jika menggunakan format ?id=
                    file_id = url_foto.split("id=")[1].split("&")[0]
                    url_foto = f"https://drive.google.com/thumbnail?id={file_id}&sz=w1000"
            
            st.image(url_foto, use_container_width=True)
            
        except Exception as e:
            st.warning("Gagal memuat gambar.")
            st.image("https://via.placeholder.com/800x600?text=Cek+Link+Foto+Anda")
        # ------------------------------------------
    st.divider()
    st.markdown("### Mengapa Bergabung dengan Tim PAS?")
    st.write("Kami berdedikasi untuk memberikan literasi keuangan terbaik bagi masyarakat.")
