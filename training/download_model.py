from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os

def download_and_save_model():
    """Downloads a pre-trained model and tokenizer and saves them locally."""

    # A pre-trained model fine-tuned for spam detection
# This is the new, correct model name
    model_name = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

    # The directory where we'll save our model and tokenizer
    save_directory = os.path.join(os.path.dirname(__file__), '..', 'models', 'spam_classifier')

    print(f"Downloading model and tokenizer for '{model_name}'...")

    # Create the directory if it doesn't exist
    os.makedirs(save_directory, exist_ok=True)

    # Download and save the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.save_pretrained(save_directory)

    # Download and save the model
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    model.save_pretrained(save_directory)

    print(f"Model and tokenizer saved to '{save_directory}'")

if __name__ == '__main__':
    download_and_save_model()