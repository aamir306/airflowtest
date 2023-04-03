from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def some_action():
  print('Valar Morghulis')

with DAG(dag_id="Dag_name",
         start_date=datetime(2023,3,13),
         schedule_interval="@daily",
         catchup=False,
         tags=["teamname", "functionality", "example"],
         ) as dag:
          
        task1 = PythonOperator(
        task_id="task_to_print",
        python_callable=some_action)


task1
