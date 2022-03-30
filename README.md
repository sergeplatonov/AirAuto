###### Install Docker Desktop (https://docs.docker.com/desktop/windows/install/)

###### Add user to workgroup docker_users: net localgroup docker-users username /ADD

###### Install Airflow with docker-compose: https://github.com/fclesio/airflow-docker-operator-with-compose

`docker-compose up airflow-init`

`docker build -f dags/Dockerfile -t registry.dg-i.net/vbmc/datascience/airflow2-dags:preprod --build-arg DAG_DIRECTORY=preprod .`

`docker-compose up -d`