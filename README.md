# MyCactus

Proyecto backend para categorizar cactus realizado con Django Rest Framework. 

## Getting Started

Estas instrucciones le proporcionarán una copia del proyecto en funcionamiento en su máquina local con fines de desarrollo y prueba.

### Prerequisites

Si quieres probar, necesitarás estos requisitos previos

```
Python > 3.6
```

### Installing

Primero, clona el proyecto en tu computadora

```
git clone https://github.com/johnLee1501/mycactus.git
```

luego, cree un entorno virtual para el proyecto, puede usar virtualenvwrapper-win si su sistema operativo es Windows

```
pip install virtualenvwrapper-win
mkvirtualenv <nombre_del_entorno>
```

después de eso, instale los paquetes en requirements.txt para asegurarse de tener todo lo necesario

```
pip install -r requirements.txt
```

finalmente, realice las migraciones correspondientes al modelo

```
py manage.py makemigrations
py manage.py migrate
```

Listo! ya puedes ejecutarlo

```
py manage.py runserver
```

Ingresa a localhost:8000/admin o localhost:8000/swagger y explora

Nota: necesitará credenciales de usuario, asegúrese de crear un usuario con

```
py manage.py createuser
```

## Authors

* **John Vega**

## Screenshots
<img src="screenshots/admin.jpg" height="400" width="800">
<img src="screenshots/admin_cactus_model.jpg" height="400" width="800">
<img src="screenshots/swagger.jpg" height="400" width="800">
