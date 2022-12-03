# Proyecto Final Computación Tolerante a Fallas

**Integrantes** 🧑‍🤝‍🧑 

- Carlos Martín García Madrigal
- Uziel Cornejo Olivares
- Christopher Iván Andrade Mendoza

# Introducción 📝

Nuestro proyecto se trata de una aplicación Web, desarrollada utilizando el framework Django. En ésta aplicación el usuario puede hacer reservaciones para un restaurante.
El propósito principal de este proyecto, es que la aplicación desarrollada sea tolerante a fallos haciendo uso de herramientas como lo son Docker, Kubernetes y OpenShift.

## Instalación local 🔨

1) Primeramente para correr nuestra aplicacion tenemos que crear un entorno virtual con python, la cual ya estando en el nos dirigimos a la carpeta de nuestro proyecto y por medio de la terminal usamos el comando python manage.py runserver el cual nos servira para correr la aplicacion.

2) Despues queremos empaquetar nuestro proyecto en docker lo cual solo tendremos que generar un archivo Dockerfile ademas de un archivo llamado requirements.txt la cual nos servira para instalar las librerias necesarias de nuestro proyecto.

3) Ahora teniendo esto tenemos que realizar algunos comandos en la terminal como docker build -t restaurant . y para ver si quedo todo perfecto tenemos que usar el comando docker run -p 8000:8000 restaurant y si ingresamos a la ruta http://127.0.0.1:8000/ nos cargara nuestra aplicacion web sin problemas, mostrandonos en la terminal las requests que hacemos.


## Implementación en OpenShift 💻

1) Debemos tener nuestro proyecto completo dentro de un repositorio en GitHub, el cual nos servirá para posteriormente poder vincularlo con la plataforma de OpenShift.
2) Habiendo hecho esto tendremos que copiar la direccion de nuestro proyecto y dirigirnos a openshift.
3) Necesitaremos de una cuenta en Openshift: https://www.redhat.com/en/technologies/cloud-computing/openshift
4) Después iremos a la sección "Add" para añadir el proyecto mediante un repositorio desde GitHub, y ponemos la direccion de nuestro repositorio junto con sus configuraciones correspondientes, incluyendo su host donde se ejecutará la Web App.
5) Esperamos a que se construya la imagen dentro de OpenShift, y se nos habra creada nuestra aplicacion en la cual podemos iniciar dandole click y veremos nuestra aplicacion web sin problemas.

Entonces ya tendremos el proyecto funcionando con Docker y kubernetes dentro de OpenShift, y dentro tenemos diferentes herramientas de monitorización para nuestro proyecto, así como funciones más avanzadas para manejar la tolerancia a fallas del programa.

![sitio1](https://user-images.githubusercontent.com/100398389/204075343-711c28d0-ee3d-4b06-89d3-ee319c2b3d2a.jpg)


## Verificamos la robustez de nuestra webApp 💻

1) Visitamos el siguiente repositorio: https://github.com/richstokes/cheekymonkey
2) Descargamos el repositorio de richstokes a nuestro ordenador, el cual contiene todos los archivos para ejecutar Cheeky Monkey.
3) Dentro de la carpeta de los archivos, ejecutamos el siguiente comando en una terminal:

pip install -r requirements.txt

De esta forma se instalará  todo lo necesario para ejecutar el programa
![image](https://user-images.githubusercontent.com/100398389/205413032-609722ca-9493-44ea-9bd4-0173c1d8fff7.png)



## Herramientas utilizadas🛠

- Django
- Docker
- Kubernetes
- Istio
- OpenShift
- Cheeky Monkey (Chaos Tools)
