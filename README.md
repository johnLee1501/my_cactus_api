# Api con Django Rest Framework (MyCactus)

Este proyecto te permite gestionar un modelo cactus a través de una Api creada con Django restframework.

### Algunas características principales: 

#### -Interfaz Swagger para realizar las operaciones básicas de un CRUD
#### -Gestión de usuarios (CRUD) 
#### -Autenticación de Django asociada a Swagger (Para poder realizar operaciones debe estar logueado)
#### -Posibilidad de subir fotografías asociadas al modelo a través de Swagger

## Previsualización

Si quieres echar un vistazo a la api antes de clonar el proyecto, puedes dirigirte a: https://cactus-api-1504.herokuapp.com/.
Utiliza las siguientes credenciales de prueba para autorizarte:

```
username: root
password: root
```


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

Ingresa a localhost:8000/

Nota: necesitará credenciales de usuario para acceder al panel de administración de Django y para poder hacer uso de los diferentes endpoints de Swagger, asegúrese de crear un usuario con

```
py manage.py createusersuperuser
```

## Autor

* **John Vega**

## Screenshots
![image](https://user-images.githubusercontent.com/71096926/120877724-be58b300-c57d-11eb-929a-8f49ae7696ae.png)
[image](https://user-images.githubusercontent.com/71096926/120877743-e21bf900-c57d-11eb-9bbb-c6024e210412.png)
![image](https://user-images.githubusercontent.com/71096926/120877781-08da2f80-c57e-11eb-91cb-d5064fe35eef.png)
