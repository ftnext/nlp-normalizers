from typing import Protocol, runtime_checkable


@runtime_checkable
class Normalizer(Protocol):
    def normalize(self, text: str) -> str:
        ...
