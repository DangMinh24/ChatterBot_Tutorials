# In this exercise, we will try to train a chatterbot, to see clearer
# how it works

# Chatterbot's training process involves loading example dialogue/
# conversation into chatterbot's database
# Then chatterbot will build upon the graph structure

# There are different type of training classes. Some of them
# were built in formal structure. Some of them you can create
# by your own

# Firstly, we try using some training classes which already have structure
# 1/Training via list data: Using list of sentence as conversation
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
# chatterbot=ChatBot("Charlie")
# chatterbot.set_trainer(ListTrainer)
#
# chatterbot.train([ #Now get a conversation to train chatterbot
#     "Hello, how can I help you?",
#     "I would like to buy ticket for a movie",
#     "Ok, for what movie?",
#     "The Wizard of Oz"]
# )
#
# chatterbot.train([
#     "Hi, how can I help you?",
#     "I would like to buy a movie ticket",
#     "Ok, for what movie?",
#     "Monty Python"
#     ]
# )

# 2/Training with corpus data
from chatterbot.trainers import ChatterBotCorpusTrainer
chatterbot=ChatBot("Marvis")
chatterbot.set_trainer(ChatterBotCorpusTrainer)
# chatterbot.train(
#     "chatterbot.corpus.english"
# )
# We can also train base on specific scope of corpus data
# chatterbot.train(
#     "chatterbot.corpus.english.greetings"
# )

# 3/Training with Twitter API
# Skip this area

# 4/Training with Ubuntu dialog corpus
# Allow chatbots to be trained with data in Ubuntu Dialog Corpus
# Skip this area

# 5/You can create a new training class: a chatbot train from your own data
# But first, we must now how to create a corpus of data for chatterbot
# To create a corpus, we must use format of json, each elements is
# a list of pair user input and bot response
# Example, in greetings.corpus.json:
# {
#   "greetings": [
#                 [
#                   "Hello",
#                   "Hi"
#                 ],
#                 [
#                   "Hi",
#                   "Hello"
#                 ],
#                 [
#                   "Hi, How is it going?",
#                   "Okay"
#                 ]
#                ]
# }
#
# You can share what this chatbot has learned with other chatbots:
# Example: If your chat bot have already learned, and saved in file export.json.
# Now you can create another chat bot, and use this database for training
# chatbot=ChatBot(New one)
# chatbot.trainer.export_for_training("./export.json")

