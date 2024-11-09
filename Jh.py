import streamlit as st

image_url = 'https://drive.google.com/thumbnail?id=1L26VEKf6ar6Bsflwh4BEKOKNowpmiY_V'

# Configura el fondo de pantalla
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('{image_url}'); /* URL de la imagen */
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la aplicación
st.write("¿Quieres saber que te quiere decir Kevy?")
st.write('Haz clic en el botón de abajo')

# Botón y mensaje
if st.button("Haz clic aquí"):
    st.title("Johana, Kevy te desea buenas noches, quiere que sepas que te ama mucho.")
