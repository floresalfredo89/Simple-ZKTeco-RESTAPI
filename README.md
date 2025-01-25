# REST API Service for ZKTeco Time Clocks

This project provides an unofficial REST API service to connect to time clocks from the brand ZKTeco. The application is implemented using Flask and deployed via Docker Compose.

## Features

- **Get Users List**: Retrieve a list of users registered in the time clock.
- **Get Attendance Records**: Obtain detailed attendance records by user and hour.
- **Check Device Current Time**: Verify the current date and time set on the device.
- **Set New Date and Time on Device**: Configure a new date and time for the time clock.

## Prerequisites

Before you begin, ensure you have installed:

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/composition/install/)

## Usage

### Build and Run the Service with Docker Compose

To build the container image and run the service, use the following commands:

```bash
docker-compose up -d
```

This command will run the application in development mode. The service will be available at `http://localhost:8080`

### Stop the Service

o stop all services running with Docker Compose, use:

```bash
docker-compose down
```

## Available Endpoints

Below are the endpoints provided by this REST API service.

- **Get Users List**
    - `GET /api/get_users`
    - Example response:
    ```json
    {
        "data": {
            "users_list": [
                {"uid": 1, "user_id": "1234", "username": "Juan Perez"}
            ]
        },
        "status": 200,
        "mimetype": "application/json"
    }
    ```

- **Get Attendance Records**
    - `GET /api/get_attendance`
    - Example response:
    ```json
    {
        "data": {
            "attendance": [
                {"uid": 1, "user_id": "1234", "timestamp": "2023-10-01T08:00:00Z"}
            ]
        },
        "status": 200,
        "mimetype": "application/json"
    }
    ```

- **Check Device Current Time**
    - `GET /api/get_time`
    - Example response:
    ```json
    {
        "data": {"current time": "2023-10-01T12:00:00"},
        "status": 200,
        "mimetype": "application/json"
    }
    ```

- **Set New Date and Time on Device**
    - `POST /api/set_time`
    - Example request:
    ```json
    {
        "time": "2023-10-01T12:00:00"
    }
    ```
    - Example response:
    ```json
    {
        "data": {"current time": "2023-10-01T12:00:00"},
        "status": 200,
        "mimetype": "application/json"
    }
    ```

## Contributions

If you would like to contribute to this project, please fork the repository and submit a pull request.


# Servicio REST API para Relojes Checadores ZKTeco

Este proyecto proporciona un servicio REST API no oficial para conectarse a relojes checadores de la marca ZKTeco. La aplicación está implementada utilizando Flask y se despliega mediante Docker Compose.

## Características

- **Obtener lista de usuarios**: Recupera la lista de usuarios registrados en el reloj checador.
- **Obtener registro de asistencia**: Obtén los registros de asistencia detallados por usuario y hora.
- **Consultar tiempo actual del dispositivo**: Verifica la hora actual establecida en el dispositivo.
- **Establecer nueva hora en el dispositivo**: Configura una nueva fecha y hora para el reloj checador.

## Requisitos Previos

Antes de iniciar, asegúrate de tener instalados:

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/composition/install/)

## Uso

### Construir y Correr el Servicio con Docker Compose

Para construir la imagen del contenedor y correr el servicio, utiliza los siguientes comandos:

```bash
docker-compose up -d
```

Este comando ejecutará la aplicación en modo de desarrollo. El servicio estará disponible en `http://localhost:8080`

### Parar el Servicio

Para detener todos los servicios que están corriendo con Docker Compose, utiliza:

```bash
docker-compose down
```

## Endpoints Disponibles

A continuación se describen los endpoints proporcionados por este servicio REST API.

- **Obtener lista de usuarios**
    - `GET /api/get_users`
    - Ejemplo de respuesta:
    ```json
    {
        "data": {
            "users_list": [
                {"uid": 1, "user_id": "1234", "username": "Juan Pérez"}
            ]
        },
        "status": 200,
        "mimetype": "application/json"
    }
    ```

- **Obtener registro de asistencia**
    - `GET /api/get_attendance`
    - Ejemplo de respuesta:
    ```json
    {
        "data": {
            "attendance": [
                {"uid": 1, "user_id": "1234", "timestamp": "2023-10-01T08:00:00Z"}
            ]
        },
        "status": 200,
        "mimetype": "application/json"
    }
    ```

- **Consultar tiempo actual del dispositivo**
    - `GET /api/get_time`
    - Ejemplo de respuesta:
    ```json
    {
        "data": {"current time": "2023-10-01T12:00:00"},
        "status": 200,
        "mimetype": "application/json"
    }
    ```

- **Establecer nueva hora en el dispositivo**
    - `POST /api/set_time`
    - Ejemplo de solicitud:
    ```json
    {
        "time": "2023-10-01T12:00:00"
    }
    ```
    - Ejemplo de respuesta:
    ```json
    {
        "data": {"current time": "2023-10-01T12:00:00"},
        "status": 200,
        "mimetype": "application/json"
    }
    ```

## Contribuciones

Si deseas contribuir a este proyecto, por favor haz un fork del repositorio y envía una solicitud de extracción (pull request).