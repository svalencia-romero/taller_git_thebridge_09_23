import streamlit as st
import os


# Para hacer deploy en streamlit, descomentar lineas de imagenes con paths correctos y comentar la linea anterior.
# Aquí va el codigo del streamlit para el taller

dir_path = os.path.dirname(os.path.realpath(__file__))

# Inicio de git, opciones y menus
st.markdown("<h1 style='text-align: center; color: black;'>Taller de Git Hub 2023</h1>", unsafe_allow_html=True) 
st.image(("../img/git_image.jpg"))
# st.image(os.path.join(dir_path,"..","img","git_image.jpg")) Para deploy
page = st.sidebar.selectbox("Selecciona una página", ("Introducción a GitHub y contenido del taller", "Comandos básicos de Git Hub", "Enlaces a repositorios"),index=None,placeholder="Selección de contenido")

def info_main():
    st.markdown ("<h2 style='text-align: center; color: black;'>Introducción a GitHub y contenido del taller</h2>",unsafe_allow_html=True)
    git_bas = st.checkbox("¿Que es Git?, ¿Que es Git Hub?, diferencias entre ambas.")
    if git_bas:
        st.markdown("###### - Git es un sistema de control de versiones distribuido. Es una herramienta que permite a los desarrolladores rastrear los cambios en su código fuente a lo largo del tiempo.")
        st.markdown("###### - GitHub, por otro lado, es una plataforma en línea que utiliza Git como motor subyacente.")
        st.markdown("###### - En resumen, Git es el sistema de control de versiones que te permite rastrear los cambios en tu código en tu computadora local, mientras que GitHub es una plataforma en línea que utiliza Git para alojar repositorios en la nube, facilitando la colaboración y la gestión de proyectos de software.")
    prim_pasos = st.checkbox("Primeros pasos en Git Hub, configuración de github en VSC y creación de repositorio")
    if prim_pasos:
        st.markdown("- Primero necesitamos configurar tu cuenta de github en el VSC, para ello entramos en la consola de VSC y ejecutamos lo siguiente(cambiando los valores de tu nombre por nombre de usuario y tu@email.com por tu email)")
        st.image(("../img/git_config.png"))
        # st.image(os.path.join(dir_path,"..","img","git_config.png")) Para deploy
        st.markdown("- Ahora crearemos nuestro repositorio, primero hay que iniciar sesión en github, hacer click en repositories para después hacer click en New")
        st.image(("../img/git_config_2.png"))
        # st.image(os.path.join(dir_path,"..","img","git_config_2.png")) Para deploy
        st.markdown("- Esta es la pantalla de creación de repositorio.")
        st.image(("../img/git_config_3.png"))
        # st.image(os.path.join(dir_path,"..","img","git_config_2.png")) Para deploy
def com_bas():
    st.markdown ("<h2 style='text-align: center; color: black;'>Comandos basicos de Git Hub</h2>",unsafe_allow_html=True)
    st.markdown("#### En este apartado tendras acceso a los comandos básicos de git hub")
    option = st.selectbox(("¿Que comando quieres utilizar?"),("ADD","Commit","Clone"),index=None,placeholder="Seleccione el comando")
    if option == "Clone":
        st.markdown ("<h2 style='text-align: center; color: black;'>Git Clone</h2>",unsafe_allow_html=True)
        st.markdown("#### Es un comando que permite realizar una copia idéntica de la última versión de un proyecto y la guarda en tu ordenador")
        st.markdown("- Primero entra en el repositorio y haz click en code")
        st.image(("../img/git_clone.png"))
        # st.image(os.path.join(dir_path,"..","img","git_clone.png")) Para deploy
        st.markdown("- Después haz click en el icono indicado y copia el enlace")
        st.image(("../img/git_clone_2.png"))
        # st.image(os.path.join(dir_path,"..","img","git_clone_2.png")) Para deploy
        st.markdown("- Antes de hacer el git clone debes añadir un espacio de trabajo nuevo.")
        st.image(("../img/git_clone_4.png"),width=400)
        # st.image(os.path.join(dir_path,"..","img","git_clone_4.png")) Para deploy
        st.markdown("- Seleccionas una carpeta que esté vacia para tu espacio de trabajo.")
        st.image(("../img/git_clone_5.png"))
        # st.image(os.path.join(dir_path,"..","img","git_clone_5.png")) Para deploy
        st.markdown("- En la consola del VSC, dentro de tu carpeta que está alojada en tu espacio de trabajo nuevo, escribe git clone <link-del-repositorio>")
        st.image(("../img/git_clone_3.png"))
        # st.image(os.path.join(dir_path,"..","img","git_clone_3.png")) Para deploy
def link_repo():
    st.markdown ("<h2 style='text-align: center; color: black;'>Enlaces a repositorios</h2>",unsafe_allow_html=True)
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
    st.link_button("Repositorio de Steven","https://github.com/TiagoValen/githubtaller_steven")

# Configuración de la página y de menu de selección de taller

if page == "Introducción a GitHub y contenido del taller":
    info_main()
elif page == "Comandos básicos de Git Hub":
    com_bas()
elif page == "Enlaces a repositorios":
    link_repo()

