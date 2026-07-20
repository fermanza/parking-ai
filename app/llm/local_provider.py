from dataclasses import dataclass

from app.llm.base import BaseLLM


@dataclass
class LocalResponse:

    content: str


class LocalProvider(BaseLLM):

    def invoke(self, prompt: str):

        text = prompt.lower()
        question = text.split("question:", 1)[-1]

        if "should a human review it" in text:
            return LocalResponse(content="NO")

        if "choose one agent" in text:
            if any(
                word in question
                for word in [
                    "reserve",
                    "reservation",
                    "book",
                    "spot"
                ]
            ):
                return LocalResponse(content="reservation")

            if any(
                word in question
                for word in [
                    "price",
                    "pricing",
                    "cost",
                    "fee",
                    "rate"
                ]
            ):
                return LocalResponse(content="pricing")

            return LocalResponse(content="support")

        return LocalResponse(content="")
