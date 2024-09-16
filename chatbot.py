from nltk.chat.util import Chat, reflections

# Define a list of patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello! How can I help you today?']),
    (r'what is your name?', ['I am a chatbot created for your college project.']),
    (r'how are you?', ['I am just a bot, but I am here to help you!']),
    (r'quit', ['Bye! Have a great day!']),
]

# Create a chatbot instance
chatbot = Chat(patterns, reflections)

def get_response(user_input):
    return chatbot.respond(user_input)

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Bye! Have a great day!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)
