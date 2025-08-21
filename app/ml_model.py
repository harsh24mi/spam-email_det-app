import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os

# --- MODEL AND TOKENIZER LOADING ---
# Define the path to the model directory
MODEL_DIR = os.path.join(os.path.dirname(__file__), '..', 'models', 'spam_classifier')

print("Loading model and tokenizer...")
try:
    # Load the tokenizer and model from the local directory
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)
    print("Model and tokenizer loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    tokenizer, model = None, None
# ------------------------------------

def predict_spam(text: str) -> str:
    """
    Takes raw text and returns a prediction using the sentiment model.
    Maps NEGATIVE sentiment to 'spam' and POSITIVE to 'not spam'.
    """
    if not model or not tokenizer:
        return "Model not loaded"
        
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    logits = outputs.logits
    predicted_class_id = torch.argmax(logits, dim=1).item()
    
    # This model's labels are 'NEGATIVE' and 'POSITIVE'
    prediction = model.config.id2label[predicted_class_id]
    
    # --- Map sentiment to our spam/not spam labels ---
    if prediction == 'NEGATIVE':
        return 'spam'
    else: # POSITIVE
        return 'not spam'