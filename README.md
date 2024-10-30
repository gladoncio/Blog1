# Proyecto Docker

Este proyecto está configurado para ejecutarse en un entorno Docker utilizando `docker-compose`. A continuación, se detallan los pasos necesarios para construir y ejecutar el proyecto.

## Requisitos

- Docker
- Docker Compose

## Instrucciones de Uso

### 1. Construcción de los contenedores

Para construir los contenedores necesarios, ejecuta el siguiente comando:

```
docker-compose build
```
Este comando lee las configuraciones del archivo docker-compose.yml y construye las imágenes necesarias para los servicios definidos.

### 2. Ejecución de los contenedores
Una vez construidas las imágenes, puedes iniciar los contenedores con el siguiente comando:

```
docker-compose up
```
Este comando levantará todos los servicios en segundo plano, permitiéndote interactuar con la aplicación en el entorno configurado.

### 3. Parar los contenedores
Para detener los contenedores, puedes utilizar Ctrl + C si los estás ejecutando en primer plano o el siguiente comando si se ejecutan en segundo plano:


```
docker-compose down
```

Esto detendrá y eliminará los contenedores que se crearon.

### Notas
Asegúrate de tener el archivo docker-compose.yml correctamente configurado antes de ejecutar los comandos.
Puedes modificar las configuraciones en docker-compose.yml según las necesidades de tu proyecto.