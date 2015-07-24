Instrucciones de instalacion
============================

La aplicación se desarrolló con Python version 2.7.3 y utiliza las herramientas virtualenv y virtualenvwrapper.
Si estos 2 últimos no están instalados, instalarlos con los siguientes comandos:

$ pip install virtualenv
$ pip install virtualenvwrapper
$ source /usr/local/bin/virtualenvwrapper.sh

Creamos un entorno virtual:

$ mkvirtualenv rentacar

Ahora estamos listos para instalar las apis de python necesarias:

$ pip install django
$ pip install djangorestframework

Y ahora las herramientas de JavaScript Node.js v0.12 y npm v2.11.3
Ejemplo en un entorno debian:

$ sudo apt-get install node npm

Nota: verificar las versiones que baja apt ya que dependiendo de la version del SO puede que no baje la version 0.12 sino una anterior, con lo cual hay que hacer lo siguiente:

$ curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash -

$ sudo apt-get install -y nodejs

Lo siguiente es clonar el repo, si es que no lo teníamos clonado de antes (se requiere tener instalado 
cliente de git)

git clone https://github.com/nachhh/alquiler-autos.git

Por último instalamos las dependencias de JavaScript (que estan declaradas en package.json y en bower.json dentro
del dir .static/rentacar) así:

$ cd/static/rentacar
$ npm install
$ npm install bower
$ bower install
$ bower install angular-daterangepicker --save (TODO agregar esto a bower.json =) )
 
Eso instala todas las dependencias necesarias para el cliente JS

Para correr el proyecto:

$ cd  alquiler-autos/
$ python manage.py runserver 

Vamos a un navegador y accedemos a:

127.0.0.1:8000/admin  --> admin de django

127.0.0.1:8000/static/rentacar/app/index.html --> cliente JS

Visitar: 
https://trello.com/b/HzN3zNvX/alquiler-autos
para ver una lista de tareas/bugs que falta resolver y en general para ver las stories.
