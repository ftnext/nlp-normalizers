from unittest.mock import MagicMock

from normalizers.base import Normalizer
from normalizers.pipeline import Pipeline


class TestPipeline:
    def test_implements_normalizer_protocol(self):
        normalizers = [MagicMock(spec=Normalizer)]
        assert isinstance(Pipeline(normalizers), Normalizer)

    def test_normalize_by_each_normalizer(self):
        normalizer1 = MagicMock(spec=Normalizer)
        normalizer2 = MagicMock(spec=Normalizer)
        sut = Pipeline([normalizer1, normalizer2])
        text = MagicMock(spec=str)

        assert sut.normalize(text) == normalizer2.normalize.return_value
        normalizer1.normalize.assert_called_once_with(text)
        normalizer2.normalize.assert_called_once_with(
            normalizer1.normalize.return_value
        )
