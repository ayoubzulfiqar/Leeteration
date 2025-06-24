import collections

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_counts = collections.Counter(text)

        balloon_req = {
            'b': 1,
            'a': 1,
            'l': 2,
            'o': 2,
            'n': 1
        }

        max_balloons = float('inf')

        for char, req_count in balloon_req.items():
            available_count = text_counts.get(char, 0)
            possible_from_char = available_count // req_count
            max_balloons = min(max_balloons, possible_from_char)

        return max_balloons