# Create a new chatbot
from chatterbot import ChatBot
# chatbot=ChatBot("Normal") # It is a name of the chatbot

# Create an Storage Adapter to connect data in different types of database
# Create simple JSONFileStorageAdapter
# chatbot=ChatBot("Normal",
#                 storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
#                 database="./database.json"
#                 )
# So we can save database in form of json

# Create an Input and Output Adapter to show how to read and how to
# express the response of the input
# chatbot=ChatBot("Normal",
#                 storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
#                 input_adapter="chatterbot.input.TerminalAdapter",
#                 output_adapter="chatterbot.output.TerminalAdapter",
#                 database="./database.json",
#                 )
# So we will read data in terminal, and print response in terminal too

# Add logic adapters
# What is a logic adapter? A logic adapter is a class that takes an input statement,
# and return a response for that statement
# We will examples two type of logic adapter :
# 1/ TimeLogicAdapter:
#   -return current time when the input statement ask about time.
# 2/ MathematicalEvaluation adapter:
#   -return result of simple math problem when input a basic operations
chatbot=ChatBot("Normal",
                storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
                input_adapter="chatterbot.input.TerminalAdapter",
                output_adapter="chatterbot.output.TerminalAdapter",
                logic_adapters=[
                    "chatterbot.logic.MathematicalEvaluation",
                    "chatterbot.logic.TimeLogicAdapter"
                ],
                database="./database.json"
                )
while True:
    try:
        bot_input=chatbot.get_response(None)

    except(KeyboardInterrupt,EOFError,SystemExit):
        break