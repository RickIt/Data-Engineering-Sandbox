from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


default_args = {
    'owner': 'ricardo',
    'retries': 5,
    'retry_delay': timedelta(minutes=5
    )
}


def greet(age,**context):
    name = context['ti'].xcom_pull(task_ids='get_name')
    print(f"Hello World! My name is {name}, "
          f"and I am {age} years old!")

def get_name():
    return 'Ricardo'


with DAG(
    default_args=default_args,
    dag_id='Minha_primeira_dag_com_python_operator_v04',
    description='Esta é minha primeira dag com python operator',
    start_date=datetime(2022, 9, 9),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        provide_context=True,
        python_callable=greet,
        op_kwargs={'age': 20}
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name        
    )

    task2 >> task1
