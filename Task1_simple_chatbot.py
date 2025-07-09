def rule_based_chatbot():
    print("🤖 Chatbot: hi! I'm your simple chatbot. Ask me anything or type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if "bye" in user_input:
            print("🤖 Chatbot: Goodbye! Have a great day.")
            break

        elif "hello" in user_input or "hi" in user_input or "namaste" in user_input:
            print("🤖 Chatbot: Hello there! How can I help you today?")

        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm just a program, but I'm doing fine. How about you?")

        elif "your name" in user_input or "whats your name" in user_input:
            print("🤖 Chatbot: I'm a simple chatbot created to help you with basic queries.")

        elif "good" in user_input:
            print("🤖 Chatbot: im happy to hear that you are doing good")
        
        elif "help" in user_input:
            print("🤖 Chatbot: Sure! You can ask about my name, how I am, or just say hello!")

        elif "weather" in user_input:
            print("🤖 Chatbot: I can't fetch real-time weather yet, but it's always sunny in here!")

        else:
            print("🤖 Chatbot: I'm sorry, I don't understand that. Can you rephrase?")

rule_based_chatbot()