from airflow import DAG
from datetime import datetime
from pokemon import extract_pokemon
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator


default_args = {
    "owner": "Brenda Schapievski",
    "start_date": datetime(2023, 3, 13),
}

dag = DAG(
    "pokemon_extraction",
    default_args=default_args,
    schedule_interval="0 10 * * *",
    max_active_runs=1,
)

start_pipeline = DummyOperator(
    task_id="start_pipeline",
    dag=dag
)

extract_pokemons = PythonOperator(
    task_id='extract_pokemons',
    python_callable=extract_pokemon,
    dag=dag
)

done_pipeline = DummyOperator(
    task_id="done_pipeline",
    dag=dag
)

start_pipeline >> extract_pokemons >> done_pipeline
