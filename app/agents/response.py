from app.agents.base import BaseAgent
from app.memory import memory_store


class ResponseAgent(BaseAgent):

    def execute(self, state):

        memory_store.append_turn(
            state["session_id"],
            state["question"],
            state.get("response") or ""
        )

        state["history"] = memory_store.get_history(
            state["session_id"]
        )

        return state
