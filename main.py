import requests

url = "http://35.193.163.40:5000/chat"

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

    if token == "food recipe":
        response = requests.post(url, json={"token": "food recipe"})
        print("Bot:", response.json()["response"])

        food_name = input("Food name: ").strip()
        response = requests.post(url, json={"token": "food recipe", "question": food_name})
        try:
            print("Bot:", response.json()["response"])
        except ValueError:
            print("Error: Server did not return valid JSON")
        continue
    # drink recipe prompt
    if token == "drink recipe":
        response = requests.post(url, json={"token": "drink recipe"})
        print("Bot:", response.json()["response"])

        # user gives drink name
        drink_name = input("Drink name: ").strip()
        response = requests.post(url, json={"token": "drink recipe", "question": drink_name})
        try:
            print("Bot:", response.json()["response"])
        except ValueError:
            print("Error: Server did not return valid JSON")
        continue

    payload = {"token": token}
    if question:
        payload["question"] = question

    response = requests.post(url, json=payload)

    # added a try block in the case of error
    try:
        if response.status_code == 200:
            print("Bot:", response.json()["response"])
        else:
            print("Error:", response.json().get("error", "Unknown error"))
    except ValueError:
        print("Error: Server did not return valid JSON")