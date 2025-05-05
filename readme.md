# Proyecto Django

Este proyecto utiliza Django como framework principal. A continuación, se detallan los pasos para instalar y configurar el entorno.

## Requisitos previos

Asegúrate de tener instalado lo siguiente:
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Virtualenv (opcional pero recomendado)

## Instalación

1. **Clona el repositorio**:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_PROYECTO>
    ```

2. **Crea un entorno virtual** (opcional pero recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. **Instala las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configura la base de datos**:
    Ejecuta las migraciones para configurar la base de datos:
    ```bash
    python manage.py migrate
    ```

5. **Inicia el servidor de desarrollo**:
    ```bash
    python manage.py runserver
    ```

## Uso

Accede al servidor de desarrollo en tu navegador en [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Notas adicionales

- Para agregar nuevas dependencias, usa:
  ```bash
  pip install <paquete>
  pip freeze > requirements.txt
  ```

- Si necesitas crear un superusuario para acceder al panel de administración de Django:
  ```bash
  python manage.py createsuperuser
  ```

¡Listo! Ahora puedes comenzar a trabajar en tu proyecto Django.