from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
import pendulum, datetime
from common_func import register2

with DAG(
    dag_id='dags_python_with_op_kwargs',
    catchup=False,
    start_date=pendulum.datetime(2023, 3, 1, tz='Asia/Seoul'),
    schedule="30 6 * * *"
) as dag:
    
    register2_t1 = PythonOperator(
        task_id="register2_t1",
        python_callable=register2,
        op_args=['jihoon', 'male', 'kr', 'seoul'],
        op_kwargs={'email':'jihoon806@gmail.com', 'phone':'010'}
    )

    register2_t1