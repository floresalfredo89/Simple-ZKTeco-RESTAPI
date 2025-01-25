# Usa una imagen base oficial de Python
FROM python:3-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos del sistema local al contenedor
COPY . /app

# Instala las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 8080 para que sea accesible desde fuera del contenedor
EXPOSE 8080

# Comando de inicio: ejecutar la aplicación Flask con Waitress
CMD ["python", "app.py"]