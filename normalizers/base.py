from typing import Protocol


class Normalizer(Protocol):
    def normalize(self, text: str) -> str:
        ...
