import random
import string

# Responses dictionary
responses = {
    "greeting": [
        "Hello! How can I help you?",
        "Hi there! What can I do for you?",
        "Hey! Nice to meet you!"
    ],
    "farewell": [
        "Goodbye! Have a great day!",
        "See you later!",
        "Bye! Take care!"
    ],
    "how_are_you": [
        "I'm doing great, thanks for asking!",
        "I'm just a bot, but I'm feeling awesome!",
        "Pretty good! How about you?"
    ],
    "name": [
        "I'm CodBot, your AI assistant!",
        "My name is CodBot!",
        "You can call me CodBot!"
    ],
    "joke": [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a fake noodle? An impasta!",
        "Why did the scarecrow win an award? He was outstanding in his field!"
    ],
    "weather": [
        "I'm not connected to weather services, but I hope it's sunny!",
        "Check weather.com for accurate updates!",
        "I wish I could tell you, but try Google Weather!"
    ],
    "age": [
        "I was just created, so I'm very young!",
        "Age is just a number for bots like me!",
        "I'm timeless! Haha!"
    ],
    "creator": [
        "I was created as part of CodSoft AI Internship!",
        "A budding AI developer made me!",
        "I was built during the CodSoft internship program!"
    ],
    "help": [
        "I can chat with you, tell jokes, and answer basic questions!",
        "Try asking me my name, a joke, or how I am!",
        "I'm here to help! Ask me anything basic!"
    ],
    "default": [
        "Hmm, I'm not sure about that. Can you rephrase?",
        "Interesting! Tell me more.",
        "I'm still learning. Try asking something else!",
        "Sorry, I didn't understand that!"
    ]
}

# Keywords mapping
keywords = {
    "greeting": ["hello", "hi", "hey", "greetings", "howdy", "sup"],
    "farewell": ["bye", "goodbye", "see you", "later", "farewell", "exit", "quit"],
    "how_are_you": ["how are you", "how r u", "how do you do", "are you okay", "how are u"],
    "name": ["your name", "who are you", "what are you", "introduce yourself"],
    "joke": ["joke", "funny", "laugh", "humor", "make me laugh"],
    "weather": ["weather", "temperature", "rain", "sunny", "climate", "forecast"],
    "age": ["how old", "your age", "age"],
    "creator": ["who made you", "who created you", "your creator", "who built you"],
    "help": ["help", "what can you do", "assist", "support"]
}

def get_response(user_input):
    user_input = user_input.lower().strip()
    
    # Remove punctuation
    user_input = user_input.translate(str.maketrans("", "", string.punctuation))
    
    # Check keywords
    for intent, words in keywords.items():
        for word in words:
            if word in user_input:
                return random.choice(responses[intent])
    
    # Default response
    return random.choice(responses["default"])

def main():
    print("=" * 40)
    print("   Welcome to CodBot - AI Chatbot!")
    print("   Type 'bye' to exit")
    print("=" * 40)
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if not user_input:
            print("CodBot: Please type something!")
            continue
        
        response = get_response(user_input)
        print(f"CodBot: {response}")
        
        # Exit condition
        if any(word in user_input.lower() for word in ["bye", "goodbye", "exit", "quit"]):
            break

if __name__ == "__main__":
    main()