from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


default_args = {
    'owner': 'ricardo',
    'retries': 5,
    'retry_delay': timedelta(minutes=5
    )
}


def greet():
    print('Hello World!')


with DAG(
    default_args=default_args,
    dag_id='Minha_primeira_dag_com_python_operator_v01',
    description='Esta é minha primeira dag com python oprator'
    start_date=datetime(2022, 9, 9)
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet
    )

    task1
