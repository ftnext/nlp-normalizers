from normalizers.base import Normalizer
from normalizers.parts import Strip


class TestStrip:
    def test_implements_normalizer_protocol(self):
        assert isinstance(Strip(), Normalizer)

    def test_can_strip(self):
        sut = Strip()

        assert sut.normalize("      テキストの前後      ") == "テキストの前後"
