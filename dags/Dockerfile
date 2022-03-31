# Build Image
FROM python:3.7

# environment variable
ARG DAG_DIRECTORY

# Create working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy the requirements for python libraries to docker container
COPY ./$DAG_DIRECTORY/requirements.txt /usr/src/app/requirements.txt

#Install all the requirements in docker container
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

#Copy the etl and config scripts
COPY ./$DAG_DIRECTORY/etl/ /usr/src/app/etl/
COPY ./resources/$DAG_DIRECTORY/environment.yml /usr/src/app/config/environment.yml
COPY ./$DAG_DIRECTORY/config /usr/src/app/config/
