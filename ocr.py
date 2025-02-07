import streamlit as st
import numpy as np
import easyocr
from PIL import Image

st.title("Reconocimiento de Texto en Imágenes (OCR) by Lucas De Rito")

# Subir imagen
uploaded_file = st.file_uploader("Sube una imagen con texto", type=["jpg", "png", "jpeg","webp"])

if uploaded_file is not None:
    # Leer la imagen y convertirla a un array de numpy
    image = Image.open(uploaded_file)
    image_np = np.array(image)

    # Utilizar EasyOCR para la extracción de texto
    reader = easyocr.Reader(["en", "es"])  # Cargar modelo para inglés y español
    extracted_text_list = reader.readtext(image_np, detail=0)
    extracted_text = "\n".join(extracted_text_list)

    # Mostrar imagen y resultado en columnas
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption="Imagen Original", use_container_width=True)
    with col2:
        # Se aumenta la altura del área de texto para mayor comodidad
        st.text_area("Texto Extraído:", extracted_text, height=600)

    # Botón para descargar el texto extraído en un archivo TXT
    st.download_button(
        label="Descargar texto como archivo TXT",
        data=extracted_text,
        file_name="texto_extraido.txt",
        mime="text/plain"
    )

