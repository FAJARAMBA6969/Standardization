import streamlit as st
from streamlit_option_menu import option_menu
from page import beranda, Pembuatan_Ls, pembuatan_Lbs, Menghitung_s


st.set_page_config(page_title="Calculator of Standardization", page_icon="🧪", layout="wide")

st.markdown("""
<style>
    section[data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.7);
        box-shadow: 0 0 20px rgba(0,0,0,0.3), 0 0 20px rgba(0,0,0,0.3);
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=[
            "Beranda",
            "Pembuatan Larutan Standar",
            "Pengenceran Larutan Standar",
            "Perhitungan Standarisasi"
        ],
        icons=["house", "eyedropper", "droplet", "calculator"],
        default_index=0
    )

st.sidebar.markdown("""
    <div style="height: 3px; background-color: rgba(255, 255, 255, 0.15); margin-top: 0px; margin-bottom: 20px;"></div>
    """, unsafe_allow_html=True)

if selected == "Beranda":
    beranda.tampil()
elif selected == "Pembuatan Larutan Standar":
    pembuatan_Lbs.tampil()
elif selected == "Pengenceran Larutan Standar":
    Pembuatan_Ls.tampil()
elif selected == "Perhitungan Standarisasi":
    Menghitung_s.tampil()
