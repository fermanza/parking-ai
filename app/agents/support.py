from app.agents.base import BaseAgent


class SupportAgent(BaseAgent):

    def execute(self, state):

        state["response"] = (
            "Support ticket created."
        )

        return state