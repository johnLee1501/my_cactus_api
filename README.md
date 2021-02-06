# Api con Django Rest Framework (MyCactus)

Este proyecto le permite gestionar  un modelo cactus a través de una Api creada con Django restframework.

### Algunas caracteristicas principales: 

#### -Interfaz Swagger para realizar las operaciones básicas de un CRUD
#### -Posibilidad de acceder al panel de administración de Django y gestionar el modelo
#### -Autenticación de Django asociada a Swagger (Para poder realizar operaciones debe estar logueado)
#### -Posibilidad de subir fotografías asociadadas al modelo a través de Swagger


## Getting Started

Estas instrucciones le proporcionarán una copia del proyecto en funcionamiento en su máquina local con fines de desarrollo y prueba.

### Prerrequisito

Si quieres probar, necesitarás estos requisitos previos

```
Python > 3.6
```

### Instalación

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

## Autor

* **John Vega**

## Screenshots
![admin](https://user-images.githubusercontent.com/71096926/106147387-c8892180-6145-11eb-9a5a-6a2a9e231a76.jpg)
![admin_cactus_model](https://user-images.githubusercontent.com/71096926/106147466-e191d280-6145-11eb-9d8d-8517f9d373c3.jpg)
![swagger](https://user-images.githubusercontent.com/71096926/106147506-eeaec180-6145-11eb-9e34-01472e8275aa.jpg)
![swagger_post](https://user-images.githubusercontent.com/71096926/106173552-0eec7980-6162-11eb-8709-0a01971266d6.png)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FjohnLee1501%2FDjango-MyCactus.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FjohnLee1501%2FDjango-MyCactus?ref=badge_shield)


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FjohnLee1501%2FDjango-MyCactus.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FjohnLee1501%2FDjango-MyCactus?ref=badge_large)