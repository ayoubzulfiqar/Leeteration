class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        result = []
        for word in words:
            parts = word.split(separator)
            for part in parts:
                if part:
                    result.append(part)
        return result