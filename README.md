# Proyecto Final Computación Tolerante a Fallas

**Integrantes** 🧑‍🤝‍🧑

- Carlos Martín García Madrigal
- Uziel Cornejo Olivares
- Christopher Iván Andrade Mendoza

# Introducción

Nuestro proyecto se trata de una aplicación Web, desarrollada utilizando el framework Django. En ésta aplicación el usuario puede hacer reservaciones para un restaurante.
El propósito principal de este proyecto, es que la aplicación desarrollada sea tolerante a fallos haciendo uso de herramientas como lo son Docker, Kubernetes y OpenShift.

## Instalación

1) Primero necesitaremos de una cuenta en Openshift: https://www.redhat.com/en/technologies/cloud-computing/openshift
2) Después iremos a la sección "Add" para añadir el proyecto mediante un repositorio desde Docker, en este caso el repositorio es: 
3) Esperamos a que se construya la imagen dentro de OpenShift, y entonces podremos acceder al sitio Web desde el enlace generado.
Entonces ya tendremos el proyecto funcionando con Docker y kubernetes dentro de OpenShift, y dentro tenemos diferentes herramientas de monitorización para nuestro proyecto, así como funciones más avanzadas para manejar la tolerancia a fallas del programa.

## Herramientas utilizadas

- Django
- Docker
- Kubernetes
- OpenShift
