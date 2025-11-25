FROM python:3.11-slim

# Establecemos el entorno de trabajo
WORKDIR /usr/src/app

# Establecemos las variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat-openbsd

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/


# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]