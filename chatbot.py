#chatbot like chatGPT

import re
from datetime import datetime

greetings = ["hi", "hello", "hey", "wre", "whr", "where"]
how_are_you = ["how are you", "how's it going", "hw r u", "hw r"]
who_are_you = ["what is your name", "who are you", "what's your name"]
help_assist = ["help", "assist"]
goodbye = ["bye", "goodbye", "goodbey"]
dob_pattern = r'(\d{4}[-/]\d{1,2}[-/]\d{1,2})|(\d{1,2}[-/]\d{1,2}[-/]\d{4})'

def calculate_age(dob):
    today = datetime.today()
    dob_date = datetime.strptime(dob, '%Y-%m-%d')
    age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
    return age

def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    if any(greeting in user_input for greeting in greetings):
        return "Hello! How can I assist you today?"
    elif any(question in user_input for question in how_are_you):
        return "I'm just a program, but I'm here to help you!"
    elif any(question in user_input for question in who_are_you):
        return "I'm a simple chatbot created to assist you!"
    elif any(question in user_input for question in help_assist):
        return "Sure! You can ask me to perform basic math operations like addition, subtraction, multiplication, and division."
    elif any(farewell in user_input for farewell in goodbye):
        return "Goodbye! Have a great day!"

    dob_match = re.search(dob_pattern, user_input)
    if dob_match:
        dob = dob_match.group(0)
        age = calculate_age(dob)
        return f"Got it! Your date of birth is {dob}. You are {age} years old."

    if re.search(r'[\d\s\+\-\*\/]+', user_input):
        try:
            result = eval(user_input)
            return f"The result is: {result}"
        except Exception:
            return "Sorry, I couldn't calculate that. Please check your input."

    return "I'm not sure how to respond to that. Can you ask something else?"

def chat():
    print("Welcome to the Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)
        if "Goodbye" in response:
            break

if __name__ == "__main__":
    chat()
