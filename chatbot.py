import random

class TeamChatbot:
    def __init__(self, team_name):
        self.team_name = team_name
        self.responses = [
            "Affirmative, {team} is on it.",
            "{team} received your message. Awaiting further instructions.",
            "{team} reporting: All clear in our sector.",
            "{team} is responding to your question.",
            "{team} acknowledges. Standing by.",
            "{team} moving to next checkpoint.",
            "{team} encountered minor resistance, proceeding as planned.",
            "{team} requests additional intel.",
            "{team} confirms: Objective secured.",
            "{team} will update in 5 minutes."
        ]

    def get_response(self, message):
        # Simple keyword-based logic, can be expanded
        if "status" in message.lower():
            return f"{self.team_name} reporting: All units operational."
        elif "support" in message.lower():
            return f"{self.team_name} requests backup at current location."
        elif "update" in message.lower():
            return f"{self.team_name} will provide update shortly."
        else:
            return random.choice([resp.format(team=self.team_name) for resp in self.responses])

# Example usage:
if __name__ == "__main__":
    bot = TeamChatbot("Bravo Team")
    while True:
        user_msg = input("Secure Message: ")
        if user_msg.lower() in ["exit", "quit"]:
            break
        print("Bot:", bot.get_response(user_msg))
