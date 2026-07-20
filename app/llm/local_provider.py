from dataclasses import dataclass

from app.llm.base import BaseLLM


@dataclass
class LocalResponse:

    content: str


class LocalProvider(BaseLLM):

    def invoke(self, prompt: str):

        text = prompt.lower()
        question = text.rsplit("question:", 1)[-1]
        history = ""

        if "conversation history:" in text and "question:" in text:
            history = text.split(
                "conversation history:",
                1
            )[1].rsplit(
                "question:",
                1
            )[0]

        if "should a human review it" in text:
            return LocalResponse(content="NO")

        if "choose one agent" in text:
            if any(
                word in question
                for word in [
                    "it",
                    "that",
                    "same",
                    "again"
                ]
            ):
                if "reservation created successfully" in history:
                    return LocalResponse(content="reservation")

                if "parking price" in history:
                    return LocalResponse(content="pricing")

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
