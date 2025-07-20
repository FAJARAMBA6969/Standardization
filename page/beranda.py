import streamlit as st
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
        return f"data:image/png;base64,{encoded}"
def tampil():
    img_data = get_base64_image("logo/logo_transparan.png")

    st.markdown(
        f"""
        <style>
        [data-testid="stHeader"] {{
            background-color: rgba(0, 0, 0, 0);    
        }}
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap');
            
        html, body, [class*="css"] {{
            font-family: 'Poppins', sans-serif;
        }}
        .logo-section {{
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 30px;
        }}
        .logo-title {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 50px;
            font-weight: bold;
            text-align: center;
            color: #c8dee8;
            margin-bottom: 0px;
            text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5)
        }}
        .logo-wrapper {{
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        [data-testid="stAppViewContainer"] {{
            background:
                radial-gradient(circle at top left, #182438 20%, transparent 80%),
                radial-gradient(circle at bottom right, #182438 3%, transparent 90%),
                radial-gradient(circle at top right, #00948a 10%, transparent 80%),
                linear-gradient(to left, #00948a, #6884a1);
        color: #c8dee8;
        }}
        .logo-wrapper img {{
            width: 300px;
            height: 300px;
            border-radius: 50%;
            object-fit: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="logo-selection">
        <div class="logo-title">Calculator of Standardization</div>
        <div class="logo-wrapper">
            <img src="{img_data}" alt="Logo Bulat">
        </div>
    </div>           
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="height: 3px; background-color: rgba(255, 255, 255, 0.1); margin-top: 0px; margin-bottom: 20px;"></div>
    """, unsafe_allow_html=True)
    st.write(
        "Calculator of Standaritation adalah web online gratis yang dirancang untuk memudahkan pengguna dalam menghitung konsentrasi larutan standar titrimetri.")
    st.write("silahkan pilih metode perhitungan yang sesuai, kemudian ikuti petunjuk yang ditampilkan dilayar!")
