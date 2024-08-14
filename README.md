<h2>Jorge Julio Suspenso Cisneros - Proyecto Final - Python #57820</h2>

La app consiste en una disquería virtual en donde podremos acceder a ella como administrador, o como cliente.

Demo: En el archivo hay un video de la app

Funcionalidades cliente:

- Registrar cliente/usuario
- Realizar el login del usuario
- Editar el perfil cliente/usuario
- Ver el catálogo de productos
- Ver el detalle de los productos
- Generar órdenes de compra
- Dar de baja órdenes de compra
- Visualizar órdenes de compra asociadas al cliente/usuario

Funcionalidades administrador:

- Realizar el login del usuario
- Ver el listado de clientes/usuarios
- Ver el detalle de un cliente/usuario
- Editar cliente/usuario
- Ver el catálogo de productos
- Agregar formatos de discos
- Agregar géneros musicales
- Agregar productos
- Editar productos
- Eliminar productos
- Ver el detalle de los productos
- Dar de baja órdenes de compra
- Visualizar todas las órdenes de compra

Se encuentra creado el usuario administrador, el cual es:

- User: Julio
- Pass: Wedamnz23

Y un usuario cliente:

- User: user
- Pass: coder2024

<h2>Instrucciones para levantar la app</h2>

- pip install pipenv
- pipenv --python <version de python>
- pipenv shell
- cd project
- pipenv install -r requirements.txt
- python manage.py migrate
- python manage.py runserver

