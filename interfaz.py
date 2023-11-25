import streamlit as st
import requests

# Título de la aplicación
st.title("Predicción de Suicidios")

# Entrada de año y mes
year = st.number_input("Ingresa el año:", min_value=2023, max_value=2050, value=2023)
month = st.number_input("Ingresa el mes:", min_value=1, max_value=12, value=11)

# Botón para realizar la predicción
if st.button("Predecir"):
    # Hacer la solicitud a la API
    url = "https://apianalitica-3c6e8fb8280e.herokuapp.com/"  # Ajusta la URL según tu configuración
    data = {"year": year, "month": month}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        resultado = response.json()
        st.write(f"Predicción para {year}-{month}: {resultado['prediccion']} intentos de suicidio")
    else:
        st.error("Error al realizar la predicción. Asegúrate de que la API esté en ejecución.")
