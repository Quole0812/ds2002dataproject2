from flask import Flask, jsonify, request
import google.generativeai as genai
import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

app = Flask(__name__)

import requests

# temp state so bot knows when user has asked for a drink recipe
drink_context = {"awaiting_drink_name": False}

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

    # cocktailAPI
    elif token == "drink recipe":
        if not question:
            # user asks for a drink recipe
            drink_context["awaiting_drink_name"] = True
            return jsonify({"response": "What drink recipe would you like to know?"})

        # user gives a drink name after being prompted
        if drink_context.get("awaiting_drink_name"):
            drink_context["awaiting_drink_name"] = False  # reset the state
            drink_name = question.strip()

            api_url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={drink_name}"
            try:
                api_response = requests.get(api_url)
                # cant reach api
                if api_response.status_code != 200:
                    return jsonify(
                        {"error": f"Failed to reach CocktailDB API (Status {api_response.status_code})"}), 500

                data = api_response.json()
                # cant find the drink
                if not data.get('drinks'):
                    return jsonify({"response": f"No cocktail recipe found for '{drink_name}'."})

                # grab the info on the drink recipe
                drink = data['drinks'][0]
                name = drink.get('strDrink', 'Unknown')
                instructions = drink.get('strInstructions', 'No instructions available')

                # get each ingredient
                ingredients = []
                for i in range(1, 16):
                    ing = drink.get(f'strIngredient{i}')
                    meas = drink.get(f'strMeasure{i}')
                    if ing:
                        line = f"{meas.strip()} {ing.strip()}" if meas else ing.strip()
                        ingredients.append(line)

                ingredient_text = '\n'.join(ingredients)
                # build the full response
                response_text = f"{name}\n\nIngredients:\n{ingredient_text}\n\nInstructions:\n{instructions}"

                # return the entire response
                return jsonify({"response": response_text})

            # if there's any other error
            except Exception as e:
                return jsonify({"error": f"Unexpected server error: {str(e)}"}), 500

        else:
            return jsonify({"response": "Please say 'drink recipe' again to start a new drink query."})

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
