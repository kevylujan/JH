import streamlit as st

# URL de la imagen
image_url = 'https://drive.google.com/thumbnail?id=1L26VEKf6ar6Bsflwh4BEKOKNowpmiY_V'

# Configura el fondo de pantalla
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{image_url}");
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
    }}
    .text-container {{
        background-color: rgba(0, 0, 0, 0.6); /* Fondo oscuro semitransparente */
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        width: 70%;
        margin: auto;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Contenedor de texto con fondo opaco
st.markdown('<div class="text-container">¿Quieres saber que te quiere decir Kevy? <br> Haz clic en el botón de abajo</div>', unsafe_allow_html=True)

# Botón y mensaje
if st.button("Haz clic aquí"):
    st.markdown('<div class="text-container"><h2>Johana, Kevy te desea buenas noches, quiere que sepas que te ama mucho.</h2></div>', unsafe_allow_html=True)
