# We know how logic adapter works, how to create a logic adapter
# But logic adapter is not only kind of adapter we must focus
# In this example, we will try to understand two kinds of adapter also important in chat bot
from chatterbot import ChatBot


#a/ Input adapter: Input adapter receive data from some source, convert it to
# datatype that chat bot can understand (Statement)
#
#
# There are lots of type of input adapter:
# 1/Variable input type: accepted input are strings,dictionaries,Statements
chatbot=ChatBot(
    "Marvis input Adapter",
    input_adapter="chatterbot.input.VariableInputTypeAdapter"
)

# 2/Terminal Adapter: accepted input which are from terminal
chatbot=ChatBot(
    "Marvis input Adapter",
    input_adapter="chatterbot.input.TerminalAdapter"
)

# There are some other kind of input adapter. However, 2 above are the most basic kinds
# We can also create our input adapter. Just like LogicAdapter, we use InputAdapter as base class

#b/ Output adapter: Output adapter show the way to express response for user
# We should focus on 2 type of output adapter:
# 1/ Output format adapter: Output return in format file
# - text: string format
# - json: dictionary
# - object: Statement object
# Example :
chatbot=ChatBot(
    "Marvis output Adapter",
    output_adapter="chatterbot.output.OutputFormatAdapter",
    output_format="text"
)

chatbot=ChatBot(
    "Marvis output Adapter",
    output_adapter="chatterbot.output.OutputFormatAdapter",
    output_format="json"
)
chatbot=ChatBot(
    "Marvis output Adapter",
    output_adapter="chatterbot.output.OutputFormatAdapter",
    output_format="object"
)

# 2/ Terminal adapter: output is response in terminal
chatbot=ChatBot(
    "Marvis output Adapter",
    output_adapter="chatterbot.output.TerminalAdapter"
)

#c/ Storage adapter: is method to save all user inputs and chat bot's responses
# 1/Json File Storage Adapter: Save conversation in JSON format file
chatbot = ChatBot(
    "Marvis Storage",
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter"
)

# 2/Mongo Database Adapter: Store data in mongoDB

#d/ Filter Adapter: Is an efficent way to create base queries that can pass into chatterbot's storage adapters
