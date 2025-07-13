from flask import Flask, request, jsonify, send_file
import joblib
from deep_translator import GoogleTranslator
import spacy
import pandas as pd
import json

app = Flask(__name__)

# Caricamento modello
import joblib

model = joblib.load("modello_rf-2.pkl")
label_encoder = joblib.load("label_encoder.pkl")
print("MODELLO CARICATO:", model)
# Caricamento sintomi
with open("symptom_keywords2.json") as f:
    symptom_keywords = json.load(f)

# NLP
nlp = spacy.load("en_core_web_sm")

from difflib import SequenceMatcher

from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()
def extract_symptoms(text, symptom_dict, threshold=0.85):
    found = set()
    text = text.lower()
    for phrase, label in symptom_dict.items():
        phrase_norm = phrase.lower().strip()
        if phrase_norm in text:
            found.add(label)
        elif SequenceMatcher(None, phrase_norm, text).ratio() >= threshold:
            found.add(label)
    return found
@app.route("/")
def serve_index():
    return send_file("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400

    input_text_it = data["text"]
    input_text_en = GoogleTranslator(source="auto", target="en").translate(input_text_it)

    print("Testo originale:", input_text_it)
    print("Testo tradotto:", input_text_en)

    symptoms_found = extract_symptoms(input_text_en, symptom_keywords)
    print("Sintomi trovati:", symptoms_found)

    if not symptoms_found:
        return jsonify({
            "predicted_disease": "Sintomi non riconosciuti. Riformula la frase.",
            "symptoms_found": []
        })

    # Riempi Symptom_1...Symptom_17 con i sintomi trovati
    symptoms_list = list(symptoms_found)
    input_dict = {f"Symptom_{i+1}": symptoms_list[i] if i < len(symptoms_list) else None for i in range(17)}
   

    df_input = pd.DataFrame([input_dict])

    # Mappatura severità
    severity_df = pd.read_csv("Symptom-severity2.csv")
    severity_dict = dict(zip(severity_df["Symptom"], severity_df["weight"]))

    # Mappa i sintomi da nome a peso
    for col in df_input.columns:
        df_input[col] = df_input[col].map(severity_dict).fillna(0)

    prediction_encoded = model.predict(df_input)[0]
    prediction = label_encoder.inverse_transform([prediction_encoded])[0]
    print("predicted_disease :", prediction)
    return jsonify({
    "predicted_disease": prediction,
    "symptoms_found": symptoms_list
})

if __name__ == "__main__":
    app.run(debug=True)