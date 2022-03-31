# Comandos básicos para trabajar con Django

A continuación usted tiene un pequeño tutorial para proceder con la instalación de:
* Un entorno virtual
* Django.
* Comandos básicos para la creación de un proyecto en Django.
* Comandos básicos para la creación de una aplicación en Django.
* Comandos básicos para preparar las migraciones en Django.
* Comandos básicos para generar las tablas en la base de datos de Django mediante ORM.
* Comandos básicos para crear un Super Usuario en Django.
* Comandos básicos para crear el archivo requirements.txt
* Comandos básicos para correr el servidor local en Django.

## Ejemplo de modelos.

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20184841.png "Django 3.1")

## Preparamos las migraciones.

Mediante el comando makemigrations preparamos las migraciones en Django

    python manage.py makemigrations

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20185052.png "Django 3.1")

## Realizamos las migraciones.

Mediante el comando migrate realizamos las migraciones en Django a la base de datos

    python manage.py migrate

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20185304.png "Django 3.1")

## Registrar el modelo en la administración de Django

En el archivo admin de la app es necesario registrar el modelo

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20190216.png "Django 3.1")

## Corremos el servidor de Django

    python manage.py runserver

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20190537.png "Django 3.1")