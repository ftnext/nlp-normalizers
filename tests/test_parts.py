from normalizers.base import Normalizer
from normalizers.parts import Strip


class TestStrip:
    def test_implements_normalizer_protocol(self):
        assert isinstance(Strip(), Normalizer)
