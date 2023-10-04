# Aquí va el codigo del streamlit para el taller
import streamlit as st
import os

git_clone = "Referencia a git clone"

dir_path = os.path.dirname(os.path.realpath(__file__))

# Inicio de git, opciones y menus.
def main(): 
    st.title("Taller de Git Hub 2023")
    st.image(os.path.join(dir_path,"..","img","git_image.jpg"),width=650)
    page = st.sidebar.selectbox("Selecciona una página", ("Información principal de Git Hub", "Comandos básicos de Git Hub", "Enlaces a repositorios"))
    
    def info_main():
        st.title ("Información principal de git hub")
        git_bas = st.checkbox("¿Que es Git?, ¿Que es Git Hub?, Diferencias entre ambas")
        if git_bas:
            st.write("Todo lo relacionado con git al inicio.")
    def com_bas():
        st.title ("Comandos basicos de Git Hub")
        st.markdown("#### En este apartado tendras acceso a los comandos básico de git hub")
        option = st.selectbox(("¿Que comando quieres utilizar?"),("ADD","Commit","Clone"),index=None,placeholder="Seleccione el comando")
    def link_repo():
        st.title ("Enlaces a repositorios")
        st.markdown ("##### Escoger el enlace correspondiente a tu nombre y aplicar un git clone al repositorio adecuado.")
        st.markdown ("###### (Solo os voy a dar acceso al repositorio indicado por lo que solo podreis acceder al repositorio que tiene vuestro nombre)")
        # Botones de enlace a cada repositorio 
        st.link_button("Repositorio de Adrian","https://github.com/TiagoValen/githubtaller_adrian")
        st.link_button("Repositorio de Águeda","https://github.com/TiagoValen/githubtaller_agueda")
        st.link_button("Repositorio de Alejandro","https://github.com/TiagoValen/githubtaller_alejandro")
        st.link_button("Repositorio de Ana","https://github.com/TiagoValen/githubtaller_ana")
        st.link_button("Repositorio de Daniel Manso","https://github.com/TiagoValen/githubtaller_danielmanso")
        st.link_button("Repositorio de Daniel Rendón","https://github.com/TiagoValen/githubtaller_danielrendon")
        st.link_button("Repositorio de Diego","https://github.com/TiagoValen/githubtaller_diego")
        st.link_button("Repositorio de Guillermo","https://github.com/TiagoValen/githubtaller_guillermo")
        st.link_button("Repositorio de Hugo","https://github.com/TiagoValen/githubtaller_hugo")
        st.link_button("Repositorio de Javier","https://github.com/TiagoValen/githubtaller_javier")
        st.link_button("Repositorio de Joan","https://github.com/TiagoValen/githubtaller_joan")
        st.link_button("Repositorio de Kino","https://github.com/TiagoValen/githubtaller_kino")
        st.link_button("Repositorio de July","https://github.com/TiagoValen/githubtaller_july")
        st.link_button("Repositorio de Luis Ángel","https://github.com/TiagoValen/githubtaller_luisangel")
        st.link_button("Repositorio de Manuel","https://github.com/TiagoValen/githubtaller_manuel")
        st.link_button("Repositorio de Maria","https://github.com/TiagoValen/githubtaller_maria")
        st.link_button("Repositorio de Matias","https://github.com/TiagoValen/githubtaller_matias")
        st.link_button("Repositorio de Miguel ","https://github.com/TiagoValen/githubtaller_miguel")
        st.link_button("Repositorio de Raimundo","https://github.com/TiagoValen/githubtaller_raimundo")
        st.link_button("Repositorio de Rodrigo","https://github.com/TiagoValen/githubtaller_rodrigo")
        st.link_button("Repositorio de Sara","https://github.com/TiagoValen/githubtaller_sara")
        st.link_button("Repositorio de Sergio","https://github.com/TiagoValen/githubtaller_sergio")
        st.link_button("Repositorio de Steven","https://github.com/TiagoValen/githubtaller_steven")
    
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