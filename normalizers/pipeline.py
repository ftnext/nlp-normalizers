from __future__ import annotations

from normalizers.base import Normalizer


class Pipeline(Normalizer):
    def __init__(self, normalizers: list[Normalizer]) -> None:
        self.normalizers = normalizers
