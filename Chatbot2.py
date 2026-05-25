#  Basic Chatbot

def chatbot():
    print(" Welcome to ChatBot!")
    print("Type 'bye' anytime to exit.\n")


    while True:
        user_input = input("You: ").lower()

        # Greetings
        if "hello" in user_input or "hi" in user_input:
            print(" ChatBot: Hello! Nice to meet you.")

        # Asking about bot
        elif "your name" in user_input:
            print("ChatBot: My name is SmartBot.")

        # Asking how are you
        elif "how are you" in user_input:
            print(" ChatBot: I'm doing great! Thanks for asking.")

           

        # Goodbye
        elif "bye" in user_input:
            print(" ChatBot: Goodbye! Have a nice day.")
            break

        # Unknown input
        else:
            print(" ChatBot: Sorry, I don't understand that.")

# Run chatbot calling function
chatbot()