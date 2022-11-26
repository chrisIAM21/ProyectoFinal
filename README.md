# Proyecto Final Computación Tolerante a Fallas

**Integrantes** 🧑‍🤝‍🧑

- Carlos Martín García Madrigal
- Uziel Cornejo Olivares
- Christopher Iván Andrade Mendoza

# Introducción

Nuestro proyecto se trata de una aplicación Web, desarrollada utilizando el framework Django. En ésta aplicación el usuario puede hacer reservaciones para un restaurante.
El propósito principal de este proyecto, es que la aplicación desarrollada sea tolerante a fallos haciendo uso de herramientas como lo son Docker, Kubernetes y OpenShift.

## Instalación local

1) Primeramente para correr nuestra aplicacion tenemos que crear un entorno virtual con python, la cual ya estando en el nos dirigimos a la carpeta de nuestro proyecto y por medio de la terminal usamos el comando python manage.py runserver el cual nos servira para correr la aplicacion.

2) Despues queremos empaquetar nuestro proyecto en docker lo cual solo tendremos que generar un archivo Dockerfile ademas de un archivo llamado requirements.txt la cual nos servira para instalar las librerias necesarias de nuestro proyecto.

3) Ahora teniendo esto tenemos que realizar algunos comandos en la terminal como docker build -t restaurant . y para ver si quedo todo perfecto tenemos que usar el comando docker run -p 8000:8000 restaurant y si ingresamos a la ruta http://127.0.0.1:8000/ nos cargara nuestra aplicacion web sin problemas, mostrandonos en la terminal las requests que hacemos.


## Implementación en OpenShift

1) Para poder correrlo en openshift primero necesitamos crear nuestra imagen de manera publica en el cloud de docker, para ello necesitaremos realizar un docker image build -t TuNombreDeUsuario/NombreDeLaImagen:IdImagen. Teniendo esto nos dirigimos a la pagino de docker.io, en la cual tendremos que iniciar sesión.
2) Habiendo hecho esto tendremos que copiar la direccion de nuestra imagen y dirigirnos a openshift
3) Necesitaremos de una cuenta en Openshift: https://www.redhat.com/en/technologies/cloud-computing/openshift
4) Después iremos a la sección "Add" para añadir el proyecto mediante un repositorio desde Docker, en este caso el repositorio es: 
5) Esperamos a que se construya la imagen dentro de OpenShift, y entonces podremos acceder al sitio Web desde el enlace generado.
Entonces ya tendremos el proyecto funcionando con Docker y kubernetes dentro de OpenShift, y dentro tenemos diferentes herramientas de monitorización para nuestro proyecto, así como funciones más avanzadas para manejar la tolerancia a fallas del programa.


## Capturas de pantalla
![dockerfile](https://user-images.githubusercontent.com/100398389/204075334-a54bab4e-86de-4b8e-b785-bd2e1e1d0f03.jpg)

![docker](https://user-images.githubusercontent.com/100398389/204075340-8d4d98a4-9ba8-4a73-aebb-5e5fdf361622.jpg)

![sitio1](https://user-images.githubusercontent.com/100398389/204075343-711c28d0-ee3d-4b06-89d3-ee319c2b3d2a.jpg)


## Herramientas utilizadas

- Django
- Docker
- Kubernetes
- OpenShift
