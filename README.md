###### Install Docker Desktop (https://docs.docker.com/desktop/windows/install/)

###### Add user to workgroup docker_users: net localgroup docker-users username /ADD

###### Install Airflow with docker-compose: https://github.com/fclesio/airflow-docker-operator-with-compose

`docker-compose up airflow-init`

`docker build -f dags/Dockerfile -t image_name --build-arg DAG_DIRECTORY=master .`

`docker-compose up -d`
