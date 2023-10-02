# Aquí va el codigo del streamlit para el taller
import streamlit as st
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

# inicio de git, opciones y menus.
def main(): 
    st.title("Taller de Git Hub 2023")
    st.image(os.path.join(dir_path,"..","img","git_image.jpg"),width=650)
    # st.sidebar.selectbox("Menu de selección de contenido")
if __name__ == "__main__":
    main()