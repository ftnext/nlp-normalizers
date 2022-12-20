from normalizers.base import Normalizer


class Strip(Normalizer):
    def normalize(self, text: str) -> str:
        return text.strip()
