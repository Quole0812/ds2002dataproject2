from flask import Flask, jsonify, request
import google.generativeai as genai
import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

app = Flask(__name__)

import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyAvpxVlA_6rjhdpR0aiYfRulS2Jbtl6NS0"
genai.configure(api_key=GOOGLE_API_KEY)

class Gemini_Chatbot:
    def __init__(self, system_prompt="You are a helpful assistant."):
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        self.history = [{"role": "model", "parts": system_prompt}]
        self.system_prompt = system_prompt

    def converse(self, user_input):
        chat = self.model.start_chat(
        history=self.history
            )
        response = chat.send_message(user_input)
        self.history.append({"role": "user", "parts": user_input})
        # print(response.text)
        self.history.append({"role": "model", "parts": response.text})
        return response.text

# kaggle API
def download_kaggle_data():
    os.environ['KAGGLE_CONFIG_DIR'] = "/path/to/your/kaggle_config_dir"  # adjust this
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('dataset-name/dataset', path='data/', unzip=True)

# fetching data from kaggle dataset
@app.route('/get-kaggle-data', methods=['GET'])
def get_kaggle_data():
    try:
        df = pd.read_csv('kaggleRecipes.csv')  
        return jsonify(df.head(10).to_dict(orient='records'))  # first 10 rows
    except Exception as e:
        return jsonify({"error": f"Error loading dataset: {str(e)}"}), 500

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    token = data.get("token", "").strip().lower()
    question = data.get("question", "").strip()

    if not token:
        return jsonify({"error": "Missing 'token' in request"}), 400

    #gemini requirement
    if token == "gemini":
        if not question:
            return jsonify({"error": "Missing 'question' for Gemini"}), 400
        chatbot = Gemini_Chatbot()
        response = chatbot.converse(question)
        return jsonify({"response": response})

    #temp for recipe
    elif token == "food recipe":
        #plz look at this
        return jsonify({"response": "Here is a sample food recipe: Tofu stir-fry"})

    #temp for drink
    elif token == "drink recipe":
        #plz look at this
        return jsonify({"response": "Here is a drink recipe: Lemonade Spritz"})

    #finish here
    elif token == "done":
        return jsonify({"response": "Session closed. Goodbye!"})

    # error handle
    else:
        return jsonify({"error": f"Unknown token: '{token}'"}), 400

# main entry point to download kaggle data
@app.before_first_request
def init_kaggle_data():
    download_kaggle_data()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
