import pandas as pd
import spacy
import json

# Carica spaCy
nlp = spacy.load("en_core_web_sm")

# Carica il file dei sintomi e descrizioni
df = pd.read_csv("dataset.csv")

# Funzione per estrarre i sintomi dalle descrizioni
def extract_keywords(description):
    doc = nlp(description.lower())
    return list(set([token.lemma_ for token in doc if token.pos_ in ["NOUN", "ADJ", "VERB"] and not token.is_stop]))

# Costruzione del dizionario
symptom_dict = {}
for _, row in df.iterrows():
    disease = row["Disease"]
    description = row["Description"]
    keywords = extract_keywords(description)
    for kw in keywords:
        if kw not in symptom_dict:
            symptom_dict[kw] = disease  # puoi anche usare un codice o etichetta sintomo

# Salvataggio in JSON
with open("symptom_keywords2.json", "w") as f:
    json.dump(symptom_dict, f, indent=2)

print(f"{len(symptom_dict)} sintomi estratti e salvati in symptom_keywords2.json")