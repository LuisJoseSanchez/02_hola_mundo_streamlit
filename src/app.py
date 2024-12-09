import streamlit as st

st.title("¡Hola mundo!")

st.write("Esta es una aplicación de prueba de Streamlit.")

nombre = st.text_input("Dime tu nombre:")

if nombre:
    st.write("¡Hola ", nombre, "!")

