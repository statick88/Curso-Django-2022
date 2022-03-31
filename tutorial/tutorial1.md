# Comandos básicos para trabajar con Django

* Creación de una aplicación nueva
* Agregar la app al archivo settings de Django.
* Creación de la primera vista.
* Creación del primer archivo urls en la app
* Agregar la url de la app al archivo urls principal del proyecto.
* Probar el servidor
* Redirigir la navegación a la ruta creada en la vista.

## Comando para crear una aplicación nueva.

    python manage.py startapp myApp

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20165450.png "Django 3.1")

## Agregar la app a settings.py.

Agregamos el nombre de la app al archivo settings de la carpeta config.

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20170055.png "Django 3.1")

## Creación de la primera Vista.

A continuación nos dirigimos al archivo views para crear nuestra primera vista.

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20170803.png "Django 3.1")

## Crear el archivo urls en la app.

Ahora es necesario crear en el directorio de la app el archivo urls que será quien reciba el string "Hello World" que pasamos como respuesta desde la vista.

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20171609.png "Django 3.1")

## Agregar la url de la app a url del proyecto.

Es necesario indicarle a nuestro proyecto principal que se ha generado una nueva url, y para ello vamos a modificar el archivo urls del directorio config.

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20082213.png "Django 3.1")

## Probamos el servidor

    python manage.py runserver

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20172625.png "Django 3.1")

#Upps

Es necesario agregar la ruta o urls al navegador 

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20174649.png "Django 3.1")

## Actualicemos la información de la Vista

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20175137.png "Django 3.1")

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20175248.png "Django 3.1")