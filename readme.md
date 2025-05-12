Requisitos para el funcionamiento del proyecto:
-Tener instalado docker  https://www.docker.com/
-Tener instalado python


Paso 1:
Clonar el repositorio en una carpet

Paso 2:
Abrir una terminal dentro del proyecto, donde estan los archivos del proyecto

Paso 3:
Ejecutrar el compando "docker compose --build"

Extras
Desde la misma terminal en el directorio del proyecto para ejecutar debes usar el siguiente formato

docker exec -it django_web python manage.py accion(migrate, makemigrations, createsuperuser, etc)
