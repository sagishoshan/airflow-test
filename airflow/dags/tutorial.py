"""
Code that goes along with the Airflow tutorial located at:
https://github.com/apache/airflow/blob/master/airflow/example_dags/tutorial.py
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG('tutorial', default_args=default_args, schedule_interval=timedelta(days=1))

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='t1_print_date',
    bash_command='date',
    dag=dag)

t2 = BashOperator(
    task_id='t2_sleep',
    bash_command='sleep 5',
    retries=3,
    dag=dag)


templated_command = """
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7)}}"
        echo "{{ params.my_param }}"
    {% endfor %}
"""

t3 = BashOperator(
    task_id='t3_templated',
    bash_command=templated_command,
    params={'my_param': 'Parameter I passed in'},
    dag=dag)

t2.set_upstream(t1)
t1 >> t3
#
# t1.set_downstream(t2)

# # This means that t2 will depend on t1
# # running successfully to run.
# # It is equivalent to:
# t2.set_upstream(t1)
#
# # The bit shift operator can also be
# # used to chain operations:
# t1 >> t2
#
# # And the upstream dependency with the
# # bit shift operator:
# t2 << t1
#
# # Chaining multiple dependencies becomes
# # concise with the bit shift operator:
# t1 >> t2 >> t3
#
# # A list of tasks can also be set as
# # dependencies. These operations
# # all have the same effect:
# t1.set_downstream([t2, t3])
# t1 >> [t2, t3]
# [t2, t3] << t1