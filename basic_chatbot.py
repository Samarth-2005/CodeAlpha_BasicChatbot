def get_bot_response(user_message):
    """Returns a predefined reply based on the user's message using if-elif-else rules."""
    msg = user_message.strip().lower()

    # Remove common punctuation from the end for cleaner matching
    msg = msg.rstrip("?!.,")

    if msg in ["hello", "hi", "hey", "greetings"]:
        return "Hi! How can I help you today?"
    elif msg in ["how are you", "how are you doing", "how do you do"]:
        return "I'm fine, thanks! How are you doing?"
    elif msg in ["i am fine", "i'm fine", "good", "great", "doing well"]:
        return "Glad to hear that! What are you working on today?"
    elif msg in ["what is your name", "who are you", "your name"]:
        return "I am the CodeAlpha Rule-Based Chatbot, built in Python!"
    elif msg in ["what can you do", "help"]:
        return (
            "You can greet me ('hello'), ask 'how are you', ask 'what is your name', "
            "ask about 'python' or 'codealpha', or type 'bye' to exit."
        )
    elif "python" in msg:
        return "Python is a powerful, beginner-friendly programming language!"
    elif "codealpha" in msg or "internship" in msg:
        return "CodeAlpha offers hands-on Python programming projects to build your skills!"
    elif msg in ["thank you", "thanks", "thx"]:
        return "You're welcome! Happy coding!"
    elif msg in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that yet. Try saying 'hello', 'how are you', 'help', or 'bye'!"


def run_chatbot():
    print("==================================================")
    print("           Welcome to the Basic Chatbot           ")
    print("==================================================")
    print("Type a message to chat (e.g., 'hello', 'how are you', 'help').")
    print("Type 'bye' anytime to end the conversation.\n")

    # Main conversation loop
    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("Bot: Please type a message so we can chat!")
            continue

        reply = get_bot_response(user_input)
        print(f"Bot: {reply}\n")

        # Exit the loop when the user says goodbye
        if user_input.strip().lower().rstrip("?!.,") in ["bye", "goodbye", "exit", "quit"]:
            break


if __name__ == "__main__":
    run_chatbot()
