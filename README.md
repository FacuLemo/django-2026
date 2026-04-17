## Instalación del proyecto
Primero, clonamos el repo. Luego:
Creamos y activamos el entorno virtual:
```
python3 -m venv venv
source venv/bin/activate
```
Instalamos Django desde el requirements
```
pip install -r requirements.txt
```
Finalmente corremos el servidor de django
```
python3 manage.py runserver
```

> IMPORTANTE: En este repo se incluye la base de datos, para que puedan usar los datos que vimos en clases. SIN EMBARGO, las bases de datos no se suelen subir a los repositorios; están definidos en el .gitignore.

## Otros comandos útiles

### Django
Iniciar un nuevo proyecto de Django (requiere tener instalado django en venv)
```
django-admin startproject comisionVirtual .
```
Iniciar una nueva aplicación
```
python3 manage.py startapp todolist
```

### Base de datos
(opcional) Si se modificó models.py, generar nuevas migraciones
```bash
python manage.py makemigrations
```
Sincronizar con la base de datos
```bash
python manage.py migrate
```
Crear un usuario para acceder al panel de administración:
```bash
python manage.py createsuperuser
```
