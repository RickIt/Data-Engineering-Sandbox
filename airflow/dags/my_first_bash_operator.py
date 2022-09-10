from datetime import datetime, timedelta
from airflow import DAG
#airflow 2.0
#from airflow.operators.bash import BashOperator

#airflow 1.10
from airflow.operators.bash_operator import BashOperator


default_args = {
    'owner': 'ricardo',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='minha_primeira_dag_v5',
    default_args=default_args,
    description='Esta é minha primeira dag',
    start_date=datetime(2022, 9, 7),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='primeira_task',
        bash_command="echo Olá Mundo, esta é a minha primeira task"
    )

    task2 = BashOperator(
        task_id='segunda_task',
        bash_command="echo hey, eu sou a segunda task e serei executada após a task1"
    )

    task3 = BashOperator(
        task_id='terceira_task',
        bash_command="""Esta é a terceira task e irá executar depois da task1 
                        e ao mesmo tempo que a task2"""
    )

    #primeiro método
    #task1.set_downstream(task2)
    #task1.set_downstream(task3)
 
    #segundo método
    task1 >> task2
    task1 >> task3

    #terceito método
    task1 >> [task2, task3]