import nltk
from nltk.chat.util import Chat, reflections

# Define a list of pattern-response pairs
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot. You can call me Messi."]
    ],
    [
        r"quit",
        ["Bye! Take care."]
    ],
]

# Create a chatbot using the pairs
chatbot = Chat(pairs, reflections)

# Start the conversation
print("Hi, I'm the chatbot. How can I assist you today?")
while True:
    user_input = input("> ")
    if user_input.lower() == "quit":
        print("Bye!, Take care.")
        break
    response = chatbot.respond(user_input)
    print(response)

