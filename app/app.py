import streamlit as st
import os


# Para hacer deploy en streamlit, descomentar lineas de imagenes con paths correctos y comentar la linea anterior.



dir_path = os.path.dirname(os.path.realpath(__file__))

# Inicio de git, opciones y menus
st.markdown("<h1 style='text-align: center;'>Taller de Git Hub 2023</h1>", unsafe_allow_html=True) 
# st.image(("../img/git_image.jpg"))
st.image(os.path.join(dir_path,"..","img","git_image.jpg")) #Para deploy

# SELECTOR DE TODO EL CONTENIDO 

page = st.sidebar.selectbox("Selecciona una página", ("Introducción a GitHub y contenido del taller", "Resumen lista comandos básicos", "Enlaces a repositorios","Ejercicio practico en grupos"),index=None,placeholder="Selección de contenido")

def info_main():
    st.markdown ("<h2 style='text-align: center;'>Introducción a GitHub y contenido del taller</h2>",unsafe_allow_html=True)

# SELECTOR CONTENIDO EN MAIN 

    option_info = st.selectbox(("¿A qué información quieres acceder?"),(["¿Que es Git?, ¿Que es Git Hub?, diferencias entre ambas.","Primeros pasos en Git Hub, configuración de github en VSC y creación de repositorio","Clonar repositorio en VSC","Como añadir nueva información a mi repositorio","Utilización y creación de ramas (branch)","Juntar ramas y actualizar cambios","Pull Request, ¿que es y para que sirve?","Resolución de conflictos"]),index=None,placeholder="Seleccione la información")
    
    if option_info == "¿Que es Git?, ¿Que es Git Hub?, diferencias entre ambas.":
        st.markdown("- Git es un sistema de control de versiones distribuido. Es una herramienta que permite a los desarrolladores rastrear los cambios en su código fuente a lo largo del tiempo.")
        st.markdown("- GitHub, por otro lado, es una plataforma en línea que utiliza Git como motor subyacente.")
        st.markdown("- En resumen, Git es el sistema de control de versiones que te permite rastrear los cambios en tu código en tu computadora local, mientras que GitHub es una plataforma en línea que utiliza Git para alojar repositorios en la nube, facilitando la colaboración y la gestión de proyectos de software.")

# CONFIG Y CREACION DE UN REPOSITORIO    

    if option_info == "Primeros pasos en Git Hub, configuración de github en VSC y creación de repositorio": # Aquí habrá dos checkbox para no meter mucha información de una vez.
        
        config_github = st.checkbox("Configuración de Github en VSC") # Primer checkbox en primeros pasos
        if config_github:
            st.markdown("- Primero necesitamos configurar tu cuenta de github en el VSC, para ello entramos en la consola de VSC y ejecutamos lo siguiente(cambiando los valores de \"Tu Nombre\" por tu nombre de usuario en Github y \"tu@email. com\" por tu email)")
            # st.image(("../img/git_config.png"))
            st.image(os.path.join(dir_path,"..","img","git_config.png")) #Para deploy
        
        new_repo = st.checkbox("Creación de repositorio") # Segundo checkbox en primeros pasos
        if new_repo:
            st.markdown("- Ahora crearemos nuestro repositorio, tenemos que iniciar sesión en github, hacer click en \"Repositories \"  para después hacer click en \"New\".")
            # st.image(("../img/git_config_2.png"))
            st.image(os.path.join(dir_path,"..","img","git_config_2.png")) #Para deploy
            st.markdown("- Esta es la pantalla de creación de repositorio.")
            # st.image(("../img/git_config_3.png"))
            st.image(os.path.join(dir_path,"..","img","git_config_3.png")) #Para deploy

# CLONAR REPOSITORIO

    if option_info == "Clonar repositorio en VSC":
        st.markdown("- Primero entra en el repositorio y haz click en code")
        # st.image(("../img/git_clone.png"))
        st.image(os.path.join(dir_path,"..","img","git_clone.png")) #Para deploy
        st.markdown("- Después haz click en el icono indicado y copia el enlace")
        # st.image(("../img/git_clone_2.png"))
        st.image(os.path.join(dir_path,"..","img","git_clone_2.png")) # Para deploy
        st.markdown("- Antes de hacer el git clone debes añadir un espacio de trabajo nuevo.")
        # st.image(("../img/git_clone_4.png"),width=400)
        st.image(os.path.join(dir_path,"..","img","git_clone_4.png")) #Para deploy
        st.markdown("- Seleccionas una carpeta que esté vacia para tu espacio de trabajo.")
        # st.image(("../img/git_clone_5.png"))
        st.image(os.path.join(dir_path,"..","img","git_clone_5.png")) #Para deploy
        st.markdown("- En la consola del VSC, dentro de tu carpeta que está alojada en tu espacio de trabajo nuevo, escribe git clone <link-del-repositorio>")
        # st.image(("../img/git_clone_3.png"))
        st.image(os.path.join(dir_path,"..","img","git_clone_3.png")) #Para deploy


# HACER ADD,COMMIT Y PUSH    

    if option_info == "Como añadir nueva información a mi repositorio": # Aquí habrá dos checkbox para no meter mucha información de una vez.
        
        añad_info_term = st.checkbox("Añadir información desde terminal") # Primer checkbox información
        if añad_info_term:
            st.markdown("- Para añadir información desde terminal, ejecutamos el siguiente comando: git add . (cuidado no olvidar el punto del final de la instrucción)")
            # st.image(("../img/add_1.png"))
            st.image(os.path.join(dir_path,"..","img","add_1.png")) #Para deploy
            st.markdown("- Una vez has añadido la información que quieres subir a tu repositorio, ejecutamos el siguiente comando: git commit -m \"mensaje que quieras añadir\"")
            # st.image(("../img/add_2.png"))
            st.image(os.path.join(dir_path,"..","img","add_2.png")) #Para deploy
            st.markdown("- Ya tenemos la información preparada y con un mensaje de los cambios que hemos hecho, los vamos a mandar a nuestro repositorio de Github con el comando: git push")
            # st.image(("../img/add_3.png"))
            st.image(os.path.join(dir_path,"..","img","add_3.png")) #Para deploy
        
        añad_info_infc = st.checkbox("Añadir información con Interface de VSC") # Segundo checkbox información
        if añad_info_infc:
            st.markdown("- Vamos añadir los archivos que aparacen en la pestaña de \"Source code\"" )
            # st.image(("../img/add_1_ejemplo_infc.png"))
            st.image(os.path.join(dir_path,"..","img","add_1_ejemplo_infc.png")) #Para deploy
            st.markdown("- Después solo hay que hacer commit & push haciendo click")
            # st.image(("../img/add_2_ejemplo_infc.png"))
            st.image(os.path.join(dir_path,"..","img","add_2_ejemplo_infc.png")) #Para deploy

# HACER BRANCH

    if option_info == "Utilización y creación de ramas (branch)": # Aquí habrá checkbox para no meter mucha información de una vez.
        añad_info_branch_1 = st.checkbox("¿Que es una rama (branch)?") # Primer checkbox branch 
        if añad_info_branch_1:
            st.markdown("- Las ramas son importantes en el desarrollo de proyectos en Github. Usando ramas, varias personas pueden trabajar en paralelo en el mismo proyecto simultáneamente. Podemos usar el comando git branch para crearlas, listarlas y eliminarlas.")
            # st.image(("../img/git_branch_merge_1.png"))
            st.image(os.path.join(dir_path,"..","img","git_branch_merge_1.png")) #Para deploy
        añad_info_branch_2 = st.checkbox("¿Como crear una rama (branch) por terminal?") # Segundo checkbox branch  
        if añad_info_branch_2:
            st.markdown("- Por terminal podemos utilizar los comandos siguientes para crear, listar y eliminar una branch en local. ")
            st.markdown("- git branch <nombre de tu branch>  - Con este comando creamos una branch en nuestro ordenador de manera local")
            st.markdown("- git branch --list - Con este comando vemos las ramas que tenemos actualmente en el repositorio")
            st.markdown("- git checkout <nombre de tu branch que has creado anteriormente> - Con este comando nos moveremos a la branch que has creado para poder trabajar en ella.")
            st.markdown("- git branch -d <nombre de tu branch que has creado anteriormente> - Con este comando podremos borrar la branch que hemos creado anteriormente(tienes que estar fuera de la branch que quieres borrar porque dará error)")
            # st.image(("../img/branch_1.png"))
            st.image(os.path.join(dir_path,"..","img","branch_1.png")) #Para deploy
            st.markdown("Al finalizar de crear la rama si quieres subir tu rama al repositorio deberás hacer dentro de la rama creada \" git push \" , en caso contrario no se subiran los cambios.")
        añad_info_branch_3 = st.checkbox("¿Como crear una rama (branch) con la interface de VSC?") # Tercer checkbox branch 
        if añad_info_branch_3:
            st.markdown("- Otra manera de hacer ramas es la siguiente:")
            st.markdown("- En la parte inferior izquierda del VSC podeis encontrar lo siguiente:")
            # st.image(("../img/branch_1_intf.jpg"))
            st.image(os.path.join(dir_path,"..","img","branch_1_intf.jpg"))#Para deploy
            st.markdown("- Al hacer click, en la parte superior se abrira un panel donde podremos crear una rama, en la misma rama donde estamos o desde otra rama concreta que queramos.")
            # st.image(("../img/branch_2_intf.jpg"))
            st.image(os.path.join(dir_path,"..","img","branch_2_intf.jpg")) #Para deploy
            st.markdown("- Una vez creada (en este caso se llama santi_prueba_2, ya aparecerá para ser selccionada y poder trabajar)")
            
            # st.image(("../img/branch_3_intf.jpg"))
            st.image(os.path.join(dir_path,"..","img","branch_3_intf.jpg")) #Para deploy
            st.markdown("- También desde el menu de Source Control lo podemos hacer:")
            # st.image(("../img/branch_1_int_sc.png"))
            st.image(os.path.join(dir_path,"..","img","branch_1_int_sc.png")) #Para deploy
            st.markdown("- En la siguiente imagen ya estamos haciendo el push de la rama a nuestro repositorio haciendo click en \"Publish Branch\"")
            # st.image(("../img/branch_2_int_sc.png"))
            st.image(os.path.join(dir_path,"..","img","branch_2_int_sc.png")) #Para deploy
            st.markdown("- Una vez ya está la rama creada de una u otra manera, podemos directamente posicionarnos sobre ella y empezar a trabajar")
            # st.image(("../img/branch_3_int_sc.png"))
            st.image(os.path.join(dir_path,"..","img","branch_3_int_sc.png")) #Para deploy

# HACER MERGE      
 
    if option_info == "Juntar ramas y actualizar cambios": # Aquí habrá dos checkbox para no meter mucha información de una vez.       
        st.markdown("* Una vez realizado el desarrollo de tu parte del proyecto en tu rama, queda fusionar la rama con la rama padre(dev o main), tienes que estar en esa rama para poder fusionar los archivos con tu rama")
        # st.image(("../img/merge_1.png"))
        st.image(os.path.join(dir_path,"..","img","merge_1.png")) # Para deploy
        st.markdown("* De la misma manera podemos hacer el merge desde la interface. (Siempre tener en cuenta desde donde estamos haciendo el merge y que queremos obtener de ello, aún así recomendable hacerlo por terminal)")
        # st.image(("../img/merge_2.png"))
        st.image(os.path.join(dir_path,"..","img","merge_2.png")) # Para deploy
            
        
# RESOLUCION DE CONFLICTOS

    if option_info == "Resolución de conflictos": # Aquí habrá dos checkbox para no meter mucha información de una vez.       
        st.markdown("* Hay veces que el código de un compañer@ entra en conflicto con el código tuyo y al intentar mezclarlos, hay que revisarlos.")
        # st.image(("../img/conflictos merge.png"))
        st.image(os.path.join(dir_path,"..","img","conflictos merge.png")) # Para deploy
        st.markdown("* Al ver el source control observamos que hay conflictos en el archivo que tendremos que resolver")
        # st.image(("../img/conflictos merge_2.png"))
        st.image(os.path.join(dir_path,"..","img","conflictos merge_2.png")) # Para deploy
        st.markdown("* Si pulsamos sobre \"Resolve in merge editor\" obtendremos la siguiente pantalla")
        # st.image(("../img/conflictos merge_3.png"))
        st.image(os.path.join(dir_path,"..","img","conflictos merge_3.png")) # Para deploy
        st.markdown("* Resolveremos los conflictos y nos dispondremos a hacer el commit")
        # st.image(("../img/conflictos merge_4.png"))
        st.image(os.path.join(dir_path,"..","img","conflictos merge_4.png")) # Para deploy
        st.markdown("* Sincronizamos los cambios y clickamos mas tarde \"OK\"")
        # st.image(("../img/conflictos merge_5.png"))
        st.image(os.path.join(dir_path,"..","img","conflictos merge_5.png")) # Para deploy
        # st.image(("../img/conflictos merge_6.png"))
        st.image(os.path.join(dir_path,"..","img","conflictos merge_6.png")) # Para deploy

# PULL REQUEST

    if option_info == "Pull Request, ¿que es y para que sirve?":
        st.markdown("* Los Pull Requests son una parte fundamental del flujo de trabajo colaborativo en el desarrollo de software. Permiten a los desarrolladores revisar, discutir y aprobar los cambios antes de que se integren en el código base principal, lo que contribuye a mantener un alto nivel de calidad y a prevenir problemas.")
        st.markdown("* Primero antes de hacer un pull request necesitamos tener todo el trabajo listo en nuestra rama y haber hecho \"push\" anteriormente, ahora seguiremos los siguiente pasos en la web")
        # st.image(("../img/pull_request_1.png"))
        st.image(os.path.join(dir_path,"..","img","pull_request_1.png")) # Para deploy
        # st.image(("../img/pull_request_1_1.png"))
        st.image(os.path.join(dir_path,"..","img","pull_request_1_1.png")) # Para deploy
        st.markdown("* Importante saber que información queremos mezclar y ver de que rama a que rama queremos pasar la información")
        # st.image(("../img/pull_request_2.png"))
        st.image(os.path.join(dir_path,"..","img","pull_request_2.png")) # Para deploy
        # st.image(("../img/pull_request_2_1.png"))
        st.image(os.path.join(dir_path,"..","img","pull_request_2_1.png")) # Para deploy
        # st.image(("../img/pull_request_3.png"))
        st.image(os.path.join(dir_path,"..","img","pull_request_3.png")) # Para deploy
        # st.image(("../img/pull_request_4.png"))
        st.image(os.path.join(dir_path,"..","img","pull_request_4.png")) # Para deploy
        st.markdown("* Una vez hecho el merge de ramas podemos borrar la rama que hemos mezclado con la principal") 
        # st.image(("../img/pull_request_5.png"))
        st.image(os.path.join(dir_path,"..","img","pull_request_5.png")) # Para deploy





# COMANDOS BÁSICOS

def com_bas():
    st.markdown ("<h2 style='text-align: center;'>Comandos basicos de Git Hub</h2>",unsafe_allow_html=True)
    st.markdown("#### En este apartado tendras acceso a los comandos básicos de git hub:")
    st.markdown("#### Clonar el repositorio")
    st.markdown("* git clone <link del repositorio>")
    st.markdown("#### Añadir un archivo concreto al repositorio")
    st.markdown("* git add <archivo>")
    st.markdown("#### Añadir todos los archivos que han cambiado al repositorio")
    st.markdown("* git add -A  (también puede añadir cambios de esta manera: \" git add . \")")
    st.markdown("#### Commit de los archivos añadidos anteriomente")
    st.markdown("* git commit -m \"<mensaje para dejar claro los cambios que estás haciendo>\"")
    st.markdown("#### Confirmar subida de archivos a repositorio")
    st.markdown("* git push")
    st.markdown("#### Actualizar los cambios de un repositorio a tu ordenador local")
    st.markdown("* git pull")
    st.markdown("#### Ver ramas actuales")
    st.markdown("* git branch --list")
    st.markdown("#### Crear una rama")
    st.markdown("* git branch <nombre de tu rama>")
    st.markdown("#### Borrar una rama")
    st.markdown("* git branch -d")
    st.markdown("#### Vemos las ramas creadas remotamente por otros usuarios")
    st.markdown("* git branch -a")
    st.markdown("#### Cambiarte a la rama que quieras")
    st.markdown("* git checkout <nombre de tu rama>")
    st.markdown("#### Crear una rama y a la vez cambiarte a la misma")
    st.markdown("* git checkout -b <nombre de la rama que quieres crear>")
    st.markdown("#### Muestra los cambios en el repositorio en orden cronologico inverso, primero la más actual a la más antigua (si quieres salir pulsa \"q\")")
    st.markdown("* git log")
    st.markdown("#### Muestra los cambios en el repositorio en orden cronologico inverso, pero en este caso solo el código de cada commit")
    st.markdown("* git log --oneline")
    st.markdown("#### Muestra información de la rama actual donde estamos trabajando")
    st.markdown("* git status")
    st.markdown("#### Deshacer un commit que nosotros queramos")
    st.markdown("* git revert <el código de commit que quieres deshacer>")
    st.markdown("#### Mezclar la información de dos ramas, siempre estando en la rama donde quieres llevar los datos de tu rama")
    st.markdown("* git merge <branch-que-quieres-mezclar>")
    


# ENLACES A REPOSITORIOS
    
        
def link_repo():
    st.markdown ("<h2 style='text-align: center;'>Enlaces a repositorios</h2>",unsafe_allow_html=True)
    st.markdown ("##### Escoger el enlace correspondiente a tu nombre y aplicar un git clone al repositorio adecuado.")
    st.markdown ("###### (Solo os voy a dar acceso al repositorio indicado por lo que solo podreis acceder al repositorio que tiene vuestro nombre)")
    # Botones de enlace a cada repositorio 
    st.link_button("Repositorio de Alicia","https://github.com/TiagoValen/githubtaller_Alicia")
    st.link_button("Repositorio de Ana","https://github.com/TiagoValen/githubtaller_Ana_")
    st.link_button("Repositorio de Javi","https://github.com/TiagoValen/githubtaller_Javi")
    st.link_button("Repositorio de Nico","https://github.com/TiagoValen/githubtaller_Nico")
    st.link_button("Repositorio de Teresa","https://github.com/TiagoValen/githubtaller_Teresa")


def ejer_grp():
    st.markdown ("Toda la información relativa a la practica grupal la teneis en el siguiente [enlace](https://github.com/svalencia-romero/taller_git_thebridge_09_23/blob/main/Practica/Ejercicio_practico_grp.pdf).")  

# Configuración de la página y de menu de selección de taller

if page == "Introducción a GitHub y contenido del taller":
    info_main()
elif page == "Resumen lista comandos básicos":
    com_bas()
elif page == "Enlaces a repositorios":
    link_repo()
elif page == "Ejercicio practico en grupos":
    ejer_grp()
    
