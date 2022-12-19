from typing import Protocol

from normalizers.base import Normalizer


class TestNormalizer:
    def test_is_protocol(self):
        assert issubclass(Normalizer, Protocol)
