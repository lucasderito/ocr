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

st.markdown('---')

st.markdown("""
### Aclaración sobre el rendimiento y despliegue

Esta aplicación está diseñada para funcionar de manera óptima en **CPU**, aunque **EasyOCR** puede aprovechar la aceleración por **GPU** si está disponible y se cuenta con una instalación de PyTorch compatible. En entornos como **Streamlit Cloud (versión gratuita)**, generalmente se utiliza CPU, lo que podría implicar tiempos de procesamiento ligeramente mayores. Se recomienda utilizar imágenes de tamaño moderado para obtener resultados más ágiles.

### Si quieren descargar el código, lo pueden encontrar en el siguiente repositorio de GitHub:  
[🔗 **OCR - GitHub**](https://github.com/lucasderito/ocr)

## Descripción de la Aplicación

Esta aplicación utiliza **EasyOCR** para realizar el reconocimiento óptico de caracteres (OCR) en imágenes. Con esta herramienta, puedes extraer texto de documentos, carteles, capturas de pantalla y cualquier imagen que contenga texto, facilitando su edición y análisis.

### Características y Técnicas Utilizadas
- **Extracción de Texto con EasyOCR:**  
  Aprovecha modelos de deep learning para detectar y reconocer texto con alta precisión, incluso en imágenes con fondos complejos.
- **Interfaz Amigable con Streamlit:**  
  Permite cargar imágenes, visualizar el texto extraído y descargarlo en un archivo TXT para un uso sencillo.
- **Soporte Multilenguaje:**  
  Configurado para reconocer textos en **inglés y español**, ampliando su utilidad en diversos contextos.

### Tipos de Imágenes Sugeridas
- **Documentos Escaneados y Fotografías de Textos:**  
  Ideal para digitalizar y procesar textos de documentos impresos o manuscritos.
- **Capturas de Pantalla y Material Publicitario:**  
  Útil para extraer información de interfaces digitales o anuncios que contengan texto.
- **Imágenes con Fondos Complejos:**  
  Gracias a EasyOCR, la aplicación puede manejar imágenes con ruido visual o fondos variados.

### Casos de Uso
#### Digitalización y Automatización
- **Conversión de Documentos a Texto:**  
  Facilita la transformación de documentos físicos en archivos editables.
- **Procesamiento Automático de Información:**  
  Permite extraer datos de facturas, recibos o formularios para integrarlos en sistemas de gestión.

#### Aplicaciones Educativas y Empresariales
- **Accesibilidad y Organización de Información:**  
  Ayuda a convertir imágenes en texto para su análisis, traducción o archivo, beneficiando tanto a estudiantes como a profesionales.
- **Integración en Flujos de Trabajo Digitales:**  
  Automatiza tareas que requieran la extracción de texto de imágenes, optimizando procesos en diversos sectores.

Esta aplicación es parte del portafolio de **Lucas De Rito**, demostrando habilidades en inteligencia artificial, visión por computadora y desarrollo de aplicaciones interactivas.

*Desarrollada con Streamlit, EasyOCR y Python.*
""")


