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
        git_bas = st.checkbox("¿Que es Git?, ¿Que es Git Hub?, Diferencias entre ambas")
        if git_bas:
            st.write("Todo lo relacionado con git al inicio.")
    def com_bas():
        st.title ("Comandos basicos de Git Hub")
    def link_repo():
        st.title ("Enlaces a repositorios")
        st.title ("Escoger el enlace a repositorio indicado y aplicar un git clone")
        adrian = st.checkbox("Repositorio de Adrian")
        if adrian:
            st.write("https://github.com/TiagoValen/githubtaller_adrian")
        
        agueda = st.checkbox("Repositorio de Águeda")
        if agueda:
            st.write("https://github.com/TiagoValen/githubtaller_agueda")
        
        alex = st.checkbox("Repositorio de Alejandro")
        if alex:
            st.write("https://github.com/TiagoValen/githubtaller_alejandro")
        
        ana = st.checkbox("Repositorio de Ana")
        if ana:
            st.write("https://github.com/TiagoValen/githubtaller_ana")
        
        daniel_manso = st.checkbox("Repositorio de Daniel Manso")
        if daniel_manso:
            st.write("https://github.com/TiagoValen/githubtaller_danielmanso")
        
        daniel_rendon = st.checkbox("Repositorio de Daniel Rendón")
        if daniel_rendon:
            st.write("https://github.com/TiagoValen/githubtaller_danielrendon")
        
        diego = st.checkbox("Repositorio de Diego")
        if diego:
            st.write("https://github.com/TiagoValen/githubtaller_diego")
        
        guillermo = st.checkbox("Repositorio de Guillermo")
        if guillermo:
            st.write("https://github.com/TiagoValen/githubtaller_guillermo")
        
        hugo = st.checkbox("Repositorio de Hugo")
        if hugo:
            st.write("https://github.com/TiagoValen/githubtaller_hugo")
        
        javier = st.checkbox("Repositorio de Javier")
        if javier:
            st.write("https://github.com/TiagoValen/githubtaller_javier")
        
        joan = st.checkbox("Repositorio de Joan")
        if joan:
            st.write("https://github.com/TiagoValen/githubtaller_joan")
        
        joaquin = st.checkbox("Repositorio de Joaquín Galvez")
        if joaquin:
            st.write("https://github.com/TiagoValen/githubtaller_kino")
        
        july = st.checkbox("Repositorio de July")
        if july:
            st.write("https://github.com/TiagoValen/githubtaller_july")
        
        luis = st.checkbox("Repositorio de Luis Ángel")
        if luis:
            st.write("https://github.com/TiagoValen/githubtaller_luisangel")
        
        manuel = st.checkbox("Repositorio de Manuel")
        if manuel:
            st.write("https://github.com/TiagoValen/githubtaller_manuel")
        
        maria = st.checkbox("Repositorio de Maria")
        if maria:
            st.write("https://github.com/TiagoValen/githubtaller_maria")
        
        matias = st.checkbox("Repositorio de Matias")
        if matias:
            st.write("https://github.com/TiagoValen/githubtaller_matias")
        
        miguel = st.checkbox("Repositorio de Miguel Ángel")
        if miguel:
            st.write("https://github.com/TiagoValen/githubtaller_miguel")
        
        raimundo = st.checkbox("Repositorio de Raimundo")
        if raimundo:
            st.write("https://github.com/TiagoValen/githubtaller_raimundo")
        
        rodrigo = st.checkbox("Repositorio de Rodrigo")
        if rodrigo:
            st.write("https://github.com/TiagoValen/githubtaller_rodrigo")
        
        sara = st.checkbox("Repositorio de Sara")
        if sara:
            st.write("https://github.com/TiagoValen/githubtaller_sara")
        
        sergio = st.checkbox("Repositorio de Sergio")
        if sergio:
            st.write("https://github.com/TiagoValen/githubtaller_sergio")
        
        steven = st.checkbox("Repositorio de Steven")
        if steven:
            st.write("https://github.com/TiagoValen/githubtaller_steven")
    
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