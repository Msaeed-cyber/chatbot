import re
import difflib
from datetime import datetime

# Log file
LOG_FILE = "chat_log.txt"

# Response dictionary (expandable)
responses = {
    # Greetings
    "hi": "Hello! How can I help you today?",
    "hello": "Hello! How can I help you today?",
    "hey": "Hey there! How can I assist you?",
    "good morning": "Good morning! What can I do for you?",
    "good afternoon": "Good afternoon! How can I help?",
    "good evening": "Good evening! How can I assist you today?",

    # Identity
    "what is your name": "I'm your AI assistant.",
    "what's your name": "I'm your AI assistant.",
    "who are you": "I'm a chatbot created to assist you.",
    "are you real": "I'm a virtual assistant powered by Python.",

    # Small talk
    "how are you": "I'm doing well, thank you! How about you?",
    "how's it going": "All good on my end. How can I assist?",
    "what's up": "Just here to help you. Ask me anything!",
    "are you okay": "I'm perfectly fine. Ready to help you.",

    # Help requests
    "can you help me": "Of course! What do you need help with?",
    "i need help": "Sure! Please tell me how I can assist you.",
    "what can you do": "I can chat, answer simple questions, and more!",

    # Farewells
    "bye": "Goodbye! Have a great day.",
    "goodbye": "Goodbye! Take care.",
    "see you": "See you next time!",
    "exit": "Goodbye! Have a great day.",
    "quit": "Goodbye! Have a great day.",

    # Thanks
    "thank you": "You're welcome!",
    "thanks": "Glad I could help!",
    "thank you so much": "Always happy to help!",
    
    # Jokes / Casual
    "tell me a joke": "Why don’t scientists trust atoms? Because they make up everything!",
    "do you like humans": "I think humans are fascinating!",
}

# Clean input
def clean_input(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text.strip()

# Time-based greeting
def get_time_greeting():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning!"
    elif 12 <= hour < 17:
        return "Good afternoon!"
    elif 17 <= hour < 22:
        return "Good evening!"
    else:
        return "Hello!"

# Get bot response
def get_response(user_input):
    cleaned = clean_input(user_input)

    # Exact match
    if cleaned in responses:
        return responses[cleaned]

    # Fuzzy match
    close_matches = difflib.get_close_matches(cleaned, responses.keys(), n=1, cutoff=0.75)
    if close_matches:
        return responses[close_matches[0]]

    return "I'm not sure how to respond to that. Can you rephrase?"

# Log conversation
def log_conversation(user, bot):
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"User: {user}\nBot: {bot}\n")

# Chat loop
def chat():
    print(get_time_greeting(), "I'm your AI assistant. Type 'exit' or 'quit' to end.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            farewell = "Goodbye! Have a great day."
            print("Bot:", farewell)
            log_conversation(user_input, farewell)
            break
        bot_reply = get_response(user_input)
        print("Bot:", bot_reply)
        log_conversation(user_input, bot_reply)

# Run chatbot
if __name__ == "__main__":
    chat()
