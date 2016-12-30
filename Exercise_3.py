# In this exercise, we will find the much closer approach to
# the core of chatterbot : Logic Adapters

# Logic Adapters determine the logic for how chat bot will response
# to a given statement
from chatterbot import ChatBot

chatbot=ChatBot(
    "Marvis",
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    logic_adapters=[
        "chatterbot.logic.BestMatch"
        #You can have multiple adapters. In that case,
        #It will try to return the response have highest
        #calculated confidence value
    ],
    database="Marvis_db.json"
)

# while True:
#     try:
#         bot_response=chatbot.get_response(None)
#
#     except(KeyboardInterrupt,EOFError,SystemExit):
#         break

# Now we will get know with different kind of logic adapter
# 1/Best match Adapter: This kind of adapter will do choosing task.
# It will find the best response based on known responses

# Okay, We will first try to understand a basic chat bot like this to see how it works
chatbot=ChatBot(
    "Marvis v2",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "response_selection_method": "chatterbot.comparisons.levenshtein_distance",
            "statement_comparison_function": "chatterbot.response_selection.get_first_response"
        }
    ]
)

# First of all, this best match logic adapter have 3 parameters
# a/ Best match to choose the best response
# b/ Comparison functions: To compare similarity between 2 statements: the input statement and the statement in database
# So how to compare 2 statements?
# Statement object represent for both input statement or statement response for input
# Response is a relationship between 2 statements
# The main key for chat bot to choose a response is based on how to choose a statement in database has some
# similarity with an input
# And there are lots of different method to compare similarity
# In this example, we use levenshtein_distance
# c/ Response selection methods: So after we get a database's statement which similar to input,
# we can get a set of responses. Now we have to determine how to select a response
# In this example, we simply choose get_first_response


# 2/Time Logic Adapter
# 3/Mathematical Evaluation Adapters
# 4/Low Confidence Response Adapters: will response a default statement if value of
# confidence is not high enough

# We will see how Low Confidence Response Aapter works:
chatbot=ChatBot(
    "Marvis v3",
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
    logic_adapters=[
        {
            "import_path":"chatterbot.logic.BestMatch"
        },
        {
            "import_path":"chatterbot.logic.LowConfidenceAdapter",
            "threshold":0.65,
            "default_response":"I am sorry, I don't get what you said :("
        }
    ],
    trainer="chatterbot.trainers.ListTrainer"
)

chatbot.train([
    'How can I help you?',
    'I want to create a chat bot',
    'Have you read the documentation?',
    'No, I have not',
    'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html'
])

response=chatbot.get_response("How can I love you?")
print(response)

# 5/Specific Response Adapter: If input match the input text specified in adapter,
# chat bot will response a specified statement
bot=ChatBot(
    "Marvis v4",
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
    logic_adapters=[
        {
            "import_path":"chatterbot.logic.BestMatch"
        },
        {
            "import_path":"chatterbot.logic.SpecificResponseAdapter",
            "input_text":"Help me!",
            "output_text":"Ok, here is a link: http://chatterbot.rtfd.org/en/latest/quickstart.html"
        },
    ],
    trainer="chatterbot.trainers.ListTrainer"
)
response=bot.get_response("Help me!")
print(response)

# Now we will come to a special case. What if our chat bot (in practical), there isn't only one
# logic adapter, but there are 2-3 logic adapters. Then each of this adapter will return one response or set of
# response(depend on what import_path you use), we must have a logic adapter to select a
# single response from responses return by all adapters
# This is where MultiLogicAdapter works