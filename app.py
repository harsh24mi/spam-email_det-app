from flask import Flask, request, render_template, session, redirect, url_for
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
import torch
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Required for session
model_dir = os.path.join(os.getcwd(), "spam_classifier_model")

tokenizer = DistilBertTokenizerFast.from_pretrained(model_dir)
model = DistilBertForSequenceClassification.from_pretrained(model_dir)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    prediction = torch.argmax(outputs.logits, dim=1).item()
    label = "SPAM" if prediction == 1 else "GENUINE"

    # Store prediction history in session
    if 'history' not in session:
        session['history'] = []
    session['history'].append({'text': text, 'label': label})
    session.modified = True

    return render_template('index.html', result=label, history=session['history'])
if __name__ == '__main__':
    app.run(debug=True)
