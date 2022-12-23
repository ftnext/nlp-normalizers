from unittest.mock import MagicMock

from normalizers.base import Normalizer
from normalizers.pipeline import Pipeline


class TestPipeline:
    def test_implements_normalizer_protocol(self):
        normalizers = [MagicMock(spec=Normalizer)]
        assert isinstance(Pipeline(normalizers), Normalizer)
