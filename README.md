# Coderhouse-47790

# Se explicarán a continuación los views que renderizan las secciones de las páginas (incluida la nueva sección para la preentrega 3)

# En el views.py de la app "cliente" tiene un apartado un index con las diferentes opciones que aún no se muestran que son los siguientes:
#                       home: el index de la sección cliente
#                       busqueda: renderiza los clientes registrados del apartado "crear" 
#                       crear: se crea mediante un registro de nombre, apellido, fecha de nacimiento y país (país Argentina creado desde el /admin/)
#                       guitarras_stock: para ver el stock de guitarras registradas en la próxima app "producto"
#                       registrar_guitarra: renderiza un formulario para registrar guitarras dentro de "guitarras_stock"

# El views.py de la app "core" representa la página de inicio y todo lo que constituye en ella:
#                       home: renderiza la página de inicio de la web
#                       about: renderiza en una de las opciones de la navbar el sobre mí, que contiene mi descripción

# Y en el views.py de la app "producto" se muestra un apartado de productos registrados:
#                       home: muestra un link de volver al inicio y te devuelve al home de "core"
#                       view_guitarras: muestra las guitarras en stock registradas por el formulario "registrar_guitarra" que se guardaron en la base de datos de ese formulario