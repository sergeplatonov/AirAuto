'''
DAG for the automatic email distribution
'''

from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from airflow.hooks.base import BaseHook
from airflow.utils.timezone import datetime
from airflow.hooks.mysql_hook import MySqlHook

# DAG definition, schedule frequency, tags
dag = DAG(
    'email',
    schedule_interval='0 7 * * *',
    catchup=False,
    start_date=datetime(2018, 1, 1),
    tags=['email']
)

# Connection with external data sources in airflow
env_variables = {'email': MySqlHook(mysql_conn_id='db_email').get_uri(),
                 }

# Docker parameters
docker_params = {'user': 'root',
                 'image': 'image_name',
                 'docker_conn_id': 'docker_default',
                 'force_pull': True,
                 'api_version': 'auto',
                 'auto_remove': True,
                 'environment': env_variables,
                 'network_mode': "bridge",
                 'dag': dag
}

# Each task is one email, the last task sends all prepared emails.
docker_params.update(task_id='plan_email',
                     command='python -c "import etl;etl.plan_email()"')
task1 = DockerOperator(**docker_params)

docker_params.update(task_id='send',
                     command='python -c "import etl;etl.send_email()"')
task2 = DockerOperator(**docker_params)

docker_params.update(task_id='log',
                     command='python -c "import etl;etl.log_email()"')
task3 = DockerOperator(**docker_params)

# Email plan tasks are parallel, Email send task is activated after all plan tasks are done
task1 >> task2 >> task3