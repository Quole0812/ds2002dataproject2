import requests

url = "http://127.0.0.1:5000/chat"

print("Chatbot client started. Type 'done' to exit.")
while True:
    token = input("Token (gemini / food recipe / drink recipe / done): ").strip().lower()

    if token == "done":
        requests.post(url, json={"token": "done"})
        print("Session ended.")
        break

    question = ""
    if token == "gemini":
        question = input("What is your question for Gemini? ")

    payload = {"token": token}
    if question:
        payload["question"] = question

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("Bot:", response.json()["response"])
    else:
        print("Error:", response.json().get("error", "Unknown error"))
