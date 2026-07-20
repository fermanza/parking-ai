from app.agents.base import BaseAgent


class ReservationAgent(BaseAgent):

    def execute(self, state):

        state["response"] = (
            "Reservation created successfully."
        )

        return state