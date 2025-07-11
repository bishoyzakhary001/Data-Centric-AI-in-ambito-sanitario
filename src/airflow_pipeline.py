from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def profiling():
    print("Profiling dei dati: statistiche, NaN, distribuzioni...")

def cleaning():
    print("Pulizia e normalizzazione sintomi...")

def augmentation():
    print("Aggiunta di nuovi esempi tramite logica manuale...")

def feature_engineering():
    print("Creazione di sintomi pesati con gravità...")

def training():
    print("Addestramento modello RandomForest/GBT...")

def evaluation():
    print("Valutazione con accuracy, F1-score e confusion matrix...")

default_args = {
    'owner': 'bishoy',
    'start_date': datetime(2025, 7, 1),
    'depends_on_past': False,
}

dag = DAG(
    'sanitary_data_centric_ai_pipeline',
    default_args=default_args,
    description='Pipeline Airflow per classificazione sintomi-malattia',
    schedule_interval=None,
    catchup=False,
)

t1 = PythonOperator(task_id='profiling', python_callable=profiling, dag=dag)
t2 = PythonOperator(task_id='cleaning', python_callable=cleaning, dag=dag)
t3 = PythonOperator(task_id='augmentation', python_callable=augmentation, dag=dag)
t4 = PythonOperator(task_id='feature_engineering', python_callable=feature_engineering, dag=dag)
t5 = PythonOperator(task_id='training', python_callable=training, dag=dag)
t6 = PythonOperator(task_id='evaluation', python_callable=evaluation, dag=dag)

t1 >> t2 >> t3 >> t4 >> t5 >> t6
