# Data-Centric-AI-in-ambito-sanitario-
Data-Centric AI in ambito sanitario: profiling, curazione e arricchimento automatico di dati sintomatici per la classificazione distribuita


 data/
    └── raw/         # CSV originale (es. symptoms_raw.csv)
    └── curated/     # Versione pulita e bilanciata
 notebooks/
    └── 01_profiling.ipynb
    └── 02_cleaning.ipynb
    └── 03_augmentation.ipynb
    └── 04_modeling_mlflow.ipynb
 src/
    └── profiling.py           # Profiling automatico (null %, class imbalance, ecc.)
    └── cleaner.py             # Tool personalizzato di data curation
    └── augmenter.py           # Tool per aggiungere sintomi logici (augmentation)
    └── pipeline.py            # Funzione principale PySpark
 mlruns/                     # Cartella di MLflow
 requirements.txt
README.md
