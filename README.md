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

Ingresa a localhost:8000/admin o localhost:8000/swagger y explore

Nota: necesitará credenciales de usuario para acceder al panel de administración de Django y para poder hacer uso de los diferentes endpoints de Swagger, asegúrese de crear un usuario con

```
py manage.py createusersuperuser
```

## Authors

* **John Vega**

## Screenshots
![admin](https://user-images.githubusercontent.com/71096926/106147387-c8892180-6145-11eb-9a5a-6a2a9e231a76.jpg)
![admin_cactus_model](https://user-images.githubusercontent.com/71096926/106147466-e191d280-6145-11eb-9d8d-8517f9d373c3.jpg)
![swagger](https://user-images.githubusercontent.com/71096926/106147506-eeaec180-6145-11eb-9e34-01472e8275aa.jpg)

