# In Exercise_3, we can see that logic adapter is a main key of
# chat bot. Despite having a lot of logic adapter API for user,
# it is better to understand how to create a new adapter

# Create a new Logic Adapter:
# Write a new class override base class LogicAdapter
from chatterbot.logic import LogicAdapter
from chatterbot import ChatBot
import random
class MyLogicAdapter(LogicAdapter):
    def __init__(self,**kwargs):
        super(MyLogicAdapter,self).__init__(kwargs)

    #There are two main function need to override:
    # 1/ can_process function: this function check whether logic adapter can process with
    # a given statement

    def can_process(self, statement):
        # Condition
        return True

    # 2/ process function: this function will return confidence value and select response statement should return

    def process(self, statement):
        confidence=random.uniform(0,1)
        return confidence,statement


# Very simple ,huh. But how we can use this new logic adapter?
# We must save this Adapter seperately, in a new file like my_adapter.py
# Then, when create a new chat bot, we can specify it like this:
# bot=ChatBot(
# #...
# logic_adapters[
#   {
#       "import_path":"my_adapter.MyLogicAdapter"
#   }
# ])

# Now we have some examples to see how it works:
# I create two small Logic Adapter:
# 1/Responding to a specific input
bot=ChatBot(
    "New Logic Adapter",
    logic_adapters=[
        {
            "import_path":"ex4_my_logic_adapter.Specific_LogicAdapter"
        }
    ]
)
response=bot.get_response("Hey Mike")
print(response)

# 2/Interacing with services
bot=ChatBot(
    "Interacting Services",
    logic_adapters=[
        {
            "import_path":"ex4_my_logic_adapter.Services_LogicAdapter"
        }
    ]
)
response=bot.get_response("what is temperature today?")
# print(response)

# 3/Providing extra arguments:
# Skip this example


