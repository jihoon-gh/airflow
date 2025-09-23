from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
import pendulum, datetime
from common_func import regist

with DAG(
    dag_id="dags_python_with_op_args",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    register_t1 = PythonOperator(
        task_id="register_t1",
        python_callable=regist,
        op_args=["jihoon", "male", "kr", "seoul"]
    )

    register_t1