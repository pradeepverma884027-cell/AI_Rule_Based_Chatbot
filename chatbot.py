print("=" *50)
print("     AI RULE-BASED CHATBOT")
print("="*50)
print()
print("Bot: Hello! I am your chatbot.")
print("Bot: Type 'bye' to exit.")
print("="*50)

while True:

    user_input = input("You: ").lower().strip()

    if user_input in ["bye","exit","quit","goodbye"]:
        print("Bot: Goodbye! Have a nice day.")
        break

    elif user_input in ["hii","hello","hey","hello","oyee"]:
        print("Bot: Hi! Nice to meet you.")

    elif user_input == "how are you":
        print("Bot: I am doing great! Thanks for asking.")

    elif user_input == "what is your name":
        print("Bot: I am a Rule-Based AI Chatbot.")

    elif user_input == "who made you":
        print("Bot: I was created using Python.")

    elif user_input=="thank you":
        print("Bot: You're welcome!")
    
    elif user_input == "good afternoon":
        print("Bot: Good Afternoon! Hope you're having a great day.")

    elif user_input == "good evening":
        print("Bot: Good Evening!")

    elif user_input == "how old are you":
        print("Bot: I don't have an age. I was created using Python.")

    elif user_input == "what can you do":
        print("Bot: I can answer simple predefined questions.")

    elif user_input == "where are you from":
        print("Bot: I live inside your computer.")

    elif user_input == "who are you":
        print("Bot: I am a Rule-Based AI Chatbot.")

    elif user_input == "what is python":
        print("Bot: Python is a popular programming language.")

    elif user_input == "what is ai":
        print("Bot: Artificial Intelligence enables machines to perform tasks that usually require human intelligence.")

    elif user_input == "who is your developer":
        print("Bot: I was developed as an internship project using Python.")
    
    elif user_input=="good morning":
        print("Bot: Good Morning! Have a wonderful day.")

    elif user_input=="good night":
        print("Bot: Good Night! Sweet dreams.")
    elif user_input == "help":
        print("\nBot: You can ask me:")
        print("- hello")
        print("- how are you")
        print("- what is your name")
        print("- what is AI")
        print("- what is Python")
        print("- who made you")
        print("- thank you")
        print("- good morning")
        print("- bye\n")
    else:
        print("Bot: Sorry, I didn't understand that. Type 'help' to see what you can ask.")
    

    