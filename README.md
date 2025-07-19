#Data-Centric AI in Healthcare

Big Data course project addressing the distributed classification of diseases from symptom descriptions.
This project follows a Data-Centric AI approach, focusing on profiling, cleaning, and automatic enrichment of symptom data to improve the quality and accuracy of the model.


#We used:
	•Apache Spark (PySpark MLlib) for preprocessing and distributed classification
	•MLflow for experiment tracking
	•Flask for the web interface
	•Random Forest and Gradient Boosted Trees for classification

##📦 Installing the requirements

##To install all dependencies:
```bash
pip3 install -r requirements.txt
```

##How it works

The symptoms_db.json file stores all information about symptoms and diseases, predicted values, and the confusion matrix.
If you want to add new symptoms, simply extend the JSON structure following the mapping defined in symptom_mapping.json.

##Example:
```json
{
    {
  "symptoms": ["fever", "cough", "fatigue"],
  "disease": "flu"
}
}
```
##Run server

To launch the web interface:
```bash
export FLASK_APP=app   # only the first time
flask run
```
##🔄 Pipeline
	1.	Data Preprocessing
	  	•Remove records with insufficient symptoms
	  	•Standardize and automatically translate symptoms
	  	•Balance underrepresented classes
	2.Distributed Training with Spark
	  	•Extract symptom-based features
	  	•Train Random Forest and GBT on Spark MLlib
	  	•Track experiments with MLflow
	3.Model Deployment
  	•Save the model as .pkl
  	•Integrate with Flask API

##Results
  	•Initial accuracy: 19% → after cleaning & enrichment → 93%
  	•Confusion matrix stored in results/confusion_matrix.png
  	•MLflow UI available for monitoring model runs

   
