# 🛡️ Spam Email Classifier (DistilBERT)

This web app classifies whether an email is spam or genuine using a fine-tuned DistilBERT model.

## 🚀 Features

- ✅ Fine-tuned transformer model (DistilBERT)
- ✅ Flask web application with clean UI
- ✅ Spam vs Genuine email classification
- ✅ Safetensors format model loading
- ✅ Fully local, no API key needed

---

## 📁 Project Structure

spam-email_det-app/
├── app.py
├── spam_classifier_model/
│ ├── config.json
│ ├── model.safetensors
│ ├── tokenizer_config.json
│ ├── tokenizer.json
│ ├── vocab.txt
│ └── special_tokens_map.json
├── static/
│ └── style.css
├── templates/
│ └── index.html
├── requirements.txt
└── README.md



---

## 📥 Download the Model

📌 Download the trained model files from the following direct link and extract them inside the `spam_classifier_model/` folder:

🔗 [Click here to download the model (Direct Link)](https://drive.google.com/uc?export=download&id=1xsoWQs-eiDlCHb1Dr6RBPh5mzK_hddrB)

Once downloaded, extract all files into:

spam-email_det-app/spam_classifier_model/



---

## 🛠️ Setup Instructions

Follow the steps below to set up and run the project:


# Clone the repository
git clone https://github.com/harsh24mi/spam-email_det-app.git
cd spam-email_det-app

# Create and activate a virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask application
python app.py

Once running, open your browser and go to:
http://127.0.0.1:5000

✅ Example Predictions
Email Text	Prediction
"You won a free iPhone! Click here to claim now."	Spam
"Let's connect for a project update meeting."	Genuine

👤 Author
Harsh Raj
harsh24mi

🌟 Show Your Support
If you found this project useful, please consider ⭐ starring the repo and sharing it with others.



