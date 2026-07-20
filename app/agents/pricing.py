from app.agents.base import BaseAgent


class PricingAgent(BaseAgent):

    def execute(self, state):

        state["response"] = (
            "Today's parking price is $12 USD."
        )

        return state