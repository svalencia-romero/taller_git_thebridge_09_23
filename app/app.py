# Aquí va el codigo del streamlit para el taller
import streamlit as st
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

# Inicio de git, opciones y menus.
def main(): 
    st.title("Taller de Git Hub 2023")
    st.image(os.path.join(dir_path,"..","img","git_image.jpg"),width=650)
    page = st.sidebar.selectbox("Selecciona una página", ("Información principal de Git Hub", "Comandos básicos de Git Hub", "Enlaces a repositorios"))
    
    def info_main():
        st.title ("Información principal de git hub")
    def com_bas():
        st.title ("Comandos basicos de Git Hub")
    def link_repo():
        st.title ("Enlaces a repositorios")
        st.title ("Escoger el enlace a repositorio indicado y aplicar un git clone")
        adrian = st.checkbox("Repositorio de Adrian Nieto Muñoz")
        if adrian:
            st.write("*Enlace a repo")
        agueda = st.checkbox("Repositorio de Águeda González Valle")
        if agueda:
            st.write("*Enlace a repo")
        alex = st.checkbox("Repositorio de Alejandro Campos Ochoa")
        if alex:
            st.write("*Enlace a repo")
        ana = st.checkbox("Repositorio de Ana Fernández de la Coba")
        if ana:
            st.write("*Enlace a repo")
        daniel_manso = st.checkbox("Repositorio de Daniel Manso Reyes")
        if daniel_manso:
            st.write("*Enlace a repo")
        daniel_rendon = st.checkbox("Repositorio de Daniel Rendón")
        if daniel_rendon:
            st.write("*Enlace a repo")
        diego = st.checkbox("Repositorio de Diego Núñez González")
        if diego:
            st.write("*Enlace a repo")
        guillermo = st.checkbox("Repositorio de Guillermo J. Pereda Pérez")
        if guillermo:
            st.write("*Enlace a repo")
        hugo = st.checkbox("Repositorio de Hugo Martín-Santos García")
        if hugo:
            st.write("*Enlace a repo")
        javier = st.checkbox("Repositorio de Javier Luis de Alcázar García")
        if javier:
            st.write("*Enlace a repo")
        joan = st.checkbox("Repositorio de Joan Salvador Calabuig")
        if joan:
            st.write("*Enlace a repo")
        joaquin = st.checkbox("Repositorio de Joaquín Galvez")
        if joaquin:
            st.write("*Enlace a repo")
        july = st.checkbox("Repositorio de July Vargas")
        if july:
            st.write("*Enlace a repo")
        luis = st.checkbox("Repositorio de Luis Ángel Soler Zamora")
        if luis:
            st.write("*Enlace a repo")
        manuel = st.checkbox("Repositorio de Manuel Reina Fernández")
        if manuel:
            st.write("*Enlace a repo")
        maria = st.checkbox("Repositorio de Maria Neches Hernandez")
        if maria:
            st.write("*Enlace a repo")
        matias = st.checkbox("Repositorio de Matias Ezequiel Ibarra")
        if matias:
            st.write("*Enlace a repo")
        miguel = st.checkbox("Repositorio de Miguel Ángel Ruíz Mico")
        if miguel:
            st.write("*Enlace a repo")
        raimundo = st.checkbox("Repositorio de Raimundo Sieso Ortiz")
        if raimundo:
            st.write("*Enlace a repo")
        rodrigo = st.checkbox("Repositorio de Rodrigo Arribas Solano")
        if rodrigo:
            st.write("*Enlace a repo")
        sara = st.checkbox("Repositorio de Sara Salguero")
        if sara:
            st.write("*Enlace a repo")
        sergio = st.checkbox("Repositorio de Sergio Rubio Cabanillas")
        if sergio:
            st.write("*Enlace a repo")
        steven = st.checkbox("Repositorio de Steven Noboa Ordóñez")
        if steven:
            st.write("*Enlace a repo")
    
    # Configuración de la página y de menu de selección de taller
    
    if page == "Información principal de Git Hub":
        info_main()
    elif page == "Comandos básicos de Git Hub":
        com_bas()
    elif page == "Enlaces a repositorios":
        link_repo()
        
    # st.sidebar.selectbox("Menu de selección de contenido")
if __name__ == "__main__":
    main()