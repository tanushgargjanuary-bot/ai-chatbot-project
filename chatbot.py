import random

def simple_chatbot():
    responses = {
        "hello": "Hello! I'm an AI assistant built by Tanush.",
        "how are you": "I'm running on code and excited to help with your AI company journey!",
        "what can you do": "I can chat, but my real purpose is demonstrating Tanush's execution skills.",
        "tell me about yourself": "I'm a Python chatbot, part of Tanush's portfolio for AI company foundations.",
        "bye": "Goodbye! Time to build the next AI breakthrough!"
    }
    
    random_responses = [
        "Interesting! Tell me more about that.",
        "I'm designed to learn from interactions. What else can we discuss?",
        "As an AI project, I'm constantly evolving. What's next?",
        "That's beyond my current training data. Let's focus on AI development!",
        "I'm here to demonstrate technical execution. Ask me about the code!"
    ]
    
    print("=== AI CHATBOT - Tanush Portfolio ===")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input == 'bye':
            print("Bot:", responses["bye"])
            break
        elif user_input in responses:
            print("Bot:", responses[user_input])
        else:
            print("Bot:", random.choice(random_responses))

simple_chatbot()