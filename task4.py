def simple_chatbot():
    print("🤖 Chatbot: Hello! Type something (type 'exit' to quit).")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("🤖 Chatbot: Hi!")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a great day 😊")
            break
        elif user_input == "exit":
            print("🤖 Chatbot: Exiting... 👋")
            break
        else:
            print("🤖 Chatbot: Sorry, I don't understand that.")

# Run the chatbot
simple_chatbot()
