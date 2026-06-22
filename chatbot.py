def get_response(user_input):
    user_input = user_input.lower().strip()
    
    if user_input in ["hello","hi", "hey"]:
        return "Hello! Nice to meet you! How can I help?"
    elif user_input in ["how are you", "how are you?", "how r u"]:
        return "I'm just a bot, but I'm running perfectly!"
    elif user_input in ["what is your name", "who are you", "your name"]:
        return "I'm RuleBot, your simple chatbot!"
    elif "help" in user_input or "what can you do" in user_input:
       return "I can respond to greetings, answer basic questions, and chat!"
    elif "time" in user_input or "date" in user_input:
        import datetime
        now = datetime.datetime.now()
        return f"Right now it's: {now.strftime('%Y-%m-%d %H:%M:%S')}"
    elif user_input in ["bye", "exit", "quit", "goodbye", "see you"]:
        return "EXIT"
    else:
        return "Sorry, I don't understand that yet. Try saying 'help'!"
    


print("=" * 40)
print("       Welcome to RuleBot!")
print("  Type 'bye' or 'exit' to quit.")
print("=" * 40)


while True:
    user_input = input("\nYou: ")

    if user_input == "":
        print("Bot: Please type something!")
        continue  

    response = get_response(user_input)

    if response == "EXIT":
        print("Bot: Goodbye! Have a wonderful day! 👋")
        break   
    else:
        print("Bot:", response)
