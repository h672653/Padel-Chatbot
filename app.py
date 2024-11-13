from flask import Flask, render_template, request, jsonify
import json
import random

app = Flask(__name__)

# Last inn regler fra JSON-filen
with open('padel.rules/rules.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

def get_response(question):
    question_lower = question.lower()

    # Sjekk hvert element i data for å finne matchende nøkkelord
    for item in data:
        if any(keyword in question_lower for keyword in item['keywords']):
            # Returner et tilfeldig svar blant mulige svar for denne intensjonen
            return random.choice(item['responses'])
    
    # Standard fallback hvis ingen nøkkelord matcher
    return "Beklager, jeg har ikke et svar på dette spørsmålet."

# Rute for nettsiden
@app.route("/")
def index():
    return render_template("index.html")

# Rute for å håndtere spørsmål via POST
@app.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question", "")
    response = get_response(question)
    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(debug=True)
