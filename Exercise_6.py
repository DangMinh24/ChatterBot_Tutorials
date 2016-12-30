# In this exercise, we will combine all kind of adapters, to create a basic outline for a chat bot

from chatterbot import ChatBot
from chatterbot.storage import JsonFileStorageAdapter
from chatterbot.input import TerminalAdapter
from chatterbot.output import TerminalAdapter
from chatterbot.trainers import ListTrainer

# Chat bot basic #1:
# -Save inputs and responses in JSON format in file "./Marvis_combine_db1.json"
# -Accept input by terminal
# -Represent output also by terminal
# -Training chat bot by conversation list
chatbot=ChatBot(
    "Marvis_combine",
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="./Marvis_combine_db1.json",
    trainer="chatterbot.trainers.ListTrainer"
)

chatbot.train([
    "Hi",
    "Hey",
    "How are you today?",
    "I'm fine. Thank you",
    "What is temperature today?",
    "Maybe 35C",
    "Are you female?",
    "I'm robot, not having gender",
    "What's your name",
    "Marvis_"
])

# How this chat bot works?
# Explain: It firstly is trained by conversation list, saved in file JSON pair statement-responses(may have many responses)
# Then it will get an input from Terminal, using some methods to compute similarity (user can specify) between input and
# statement in file JSON. It then will get a set of responses for statement
# Now it will use a specific method to get a best response in this set of responses.
# Every time like that, it will update statement and response

# In chat bot #1, we only use default logic_adapter, so we can not see how it compares similarity and choose response
# However, users have a power to change the way chat bot comparing 2 statements, or picking the best response by logic_adapter

# Chat bot basic #2:
chatbot=ChatBot(
    "Marvis_combine_v2",
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    trainer="chatterbot.trainers.ListTrainer",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.jaccard_similarity",
            "response_selection_method": "chatterbot.response_selection.get_first_response"
        },
    ],

    database="./Marvis_combine_db2.json",
)
from chatterbot.comparisons import jaccard_similarity
chatbot.train([
    "Hi",
    "Hey",
    "How are you today?",
    "I'm fine. Thank you",
    "What is temperature today?",
    "Maybe 35C",
    "Are you female?",
    "I'm robot, not having gender",
    "What's your name",
    "Marvis_"
])

# Chat bot basic #3: Using trainer with corpus (JSON file):
chatbot=ChatBot(
    "Marvis_combine_v3",
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    trainer="chatterbot.trainers.ChatterBotCorpusTrainer",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_first_response"
        }
    ],
    database="./Marvis_combine_db3.json"
)
# There are two method to train JSON file
# 1/You can use a corpus that define in chatterbot:
# chatbot.train("chatterbot.corpus.english")
# Despite the path for data is chatterbot.corpus.data.english

# 2/You can use a trainer.export_for_training function to get a conversation in JSON file
chatbot.trainer.export_for_training("./simple_db.json")

# while True:
#     try:
#         response=chatbot.get_response(None)
#     except(KeyboardInterrupt,EOFError,SystemExit):
#         break


# You can get a lot of further ideas with chatterbot:
# + You can create a bigger corpus (all corpus in this project is small). You can make your chat bot more "clever" and "funnier"
# + If you interested in building a application, you can integrate with MongoDB and working in server clients side.
# + We can use an idea in Retrieval-based Bot, using RNN to train algorithm that help chat bot choose a best response

