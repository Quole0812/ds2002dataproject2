from flask import Flask, jsonify, request
import google.generativeai as genai


app = Flask(__name__)


import google.generativeai as genai

# Example Set Up of the API key stored in Google Colab secret keys
GOOGLE_API_KEY = "AIzaSyAvpxVlA_6rjhdpR0aiYfRulS2Jbtl6NS0"
genai.configure(api_key=GOOGLE_API_KEY)

class Gemini_Chatbot:
    def __init__(self, system_prompt="You are a helpful assistant."):
        self.model = genai.GenerativeModel("gemini-1.5-flash") #choose your model here
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

    # Handle food recipe (stub)
    elif token == "food recipe":
        # Replace with real API call later
        return jsonify({"response": "Here is a sample food recipe: Tofu stir-fry"})

    # Handle drink recipe (stub)
    elif token == "drink recipe":
        # Replace with real API call later
        return jsonify({"response": "Here is a drink recipe: Lemonade Spritz"})

    # Done signal
    elif token == "done":
        return jsonify({"response": "Session closed. Goodbye!"})

    # Unknown
    else:
        return jsonify({"error": f"Unknown token: '{token}'"}), 400



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)


