#Comandos básicos para trabajar con Django

## Comando para conocer la versión de Python instalada.

    python -V

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20075708.png "Django 3.1")

## Crear un nuevo directorio.

    mkdir project_name

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20075948.png "Django 3.1")
## Crear entorno virtual.

    python -m venv .env

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20081536.png "Django 3.1")

## Activar el entorno virtual en GNU/Linux o Mac o Git en Windows.

    source .env/bin/activate
![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20081733.png "Django 3.1")
## Activar el entorno virtual en Windows.

    cd .env/Scrtipts

    activate

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20082213.png "Django 3.1")
## Instalar Django

    pip install django

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20082601.png "Django 3.1")
Siempre y cuando se desee instalar la última versión estable, caso contrario utilizar el siguiente comando.

    pip install django==version.de.django

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20082740.png "Django 3.1")
Donde "version.de.django" permite introducir la versión de python que se desea utilizar.

## Crear proyecto nuevo de Django

    django-admin startproject nombre_del_proyecto
![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20082855.png "Django 3.1")
Por lo general se acostumbra a crear el proyecto de esta forma, pero existe una mejor alternativa que permite evitar la duplicidad de información (directorios) al momento de crear el proyecto general.

    django-admin startproject config .

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20082855.png "Django 3.1")
En este caso se reconoce el directorio donde se encuentra en ese momento el tutorial.

## Crear app en Django.

    python manage.py startproject app_name
![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20083150.png "Django 3.1")
## Crear las primeras migraciones.

    python manage.py makemigrations
![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20083346.png "Django 3.1")
## Realizar las primeras migraciones en las bases de datos y las tablas.

    python manage.py migrate

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20083508.png "Django 3.1")

## Crear superusuario.

    python manage.py createsuperuser

Debe proveer información necesaria al sistema como:

* Nombre de Usuario.
* Correo Electrónico (no indispensable por el momento).
* Password (Se recomienda una contraseña mayor a 8 digitos, combinar mayusculas y minustuclas, numeros y simbolos especiales).

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20083650.png "Django 3.1")

## Crear el archivo requirements.txt

    pip freeze

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20083743.png "Django 3.1")

El comando pip freeze, provee información básica al usuario de los diferentes paquetes, plugins o librerias instaladas en el entorno virtual.

    pip freeze > requirements.txt

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20083921.png "Django 3.1")

Este comando pasa como parametro información básica al archivo requirements.txt acerca de los paquetes, plugins o librerías instaladas hasta el momento en el entorno virtual.

Despues de cada cambio en el archivo models es necesario actualizar este archivo si es necesario.

Si es necesario la instalación de archivos desde requirements.txt se recomienda utilizar este comando en un ambiente diferente (Por ejemplo un Deploy en Producción o un programador diferente).

    pip install -r requirements.txt

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20084046.png "Django 3.1")

## Otros comandos útiles
Existen muchos comandos que se puede utilizar para mejorar el proyecto, puede conocerlos mediante el siguiente comando

    django-admin

Mediante este comando aparecerá una salida con todas las posibles combinaciones.

    Available subcommands:

    [django]
        check
        compilemessages
        createcachetable
        dbshell
        diffsettings
        dumpdata
        flush
        inspectdb
        loaddata
        makemessages
        makemigrations
        migrate
        runserver
        sendtestemail
        shell
        showmigrations
        sqlflush
        sqlmigrate
        sqlsequencereset
        squashmigrations
        startapp
        startproject
        test
        testserver

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20084221.png "Django 3.1")

# Finalmente

Si queremos probar nuestro Django de forma local, debemos utilizar el comandoL:

    python manage.py runserver

Esto permitirá activar un servidor local que viene incluido en Django.

![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20084356.png "Django 3.1")

Servidor Corriendo en localhost a traves del puerto 8000
![Django 4.0](/tutorial/media/Screenshot%202022-03-30%20091523.png "Django 3.1")

Para detener el servidor teclee:

    Ctrl + c

# Extra

Por si es necesario subir el código a un respositorio en github, se recomienda agregar a la raiz del proyecto el archivo .gitignore

Lo puede hacer copiando y pegando el contenido de esta url https://github.com/jpadilla/django-project-template/blob/master/.gitignore