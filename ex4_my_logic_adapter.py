from chatterbot.logic import LogicAdapter

class Specific_LogicAdapter(LogicAdapter):

    def can_process(self, statement):
        if statement.text.startswith("Hey Mike"):
            return True
        else:
            return False
    def process(self, statement):
        confidence=1
        select_statement=statement
        return confidence,statement

class Services_LogicAdapter(LogicAdapter):
    def can_process(self, statement):
        words=["what","is","temperature"]

        if all(x in statement.text.split() for x in words):
            return True
        else:
            return False
    def process(self, statement):
        from chatterbot.conversation import Statement
        import requests

        response=requests.get("https://api.temperature.com/current?units=celsius") # this link is broken,
        # may lead to error,I still don't know a replacement, so I keep the same link here
        data=response.json()

        if response.status_code==200:
            confidence=1
        else:
            confidence=0

        temperature=data.get("temperature","unavailable")

        response_statement=Statement("The current temperature is {}".format(temperature))

        return confidence,response_statement

