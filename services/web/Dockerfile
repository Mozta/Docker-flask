FROM python:3.11-slim-buster

# Establecemos el entorno de trabajo
WORKDIR /usr/src/app

# Establecemos las variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalamos las dependencias del sistema
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# Copiamos el código de la aplicación
COPY . /usr/src/app/