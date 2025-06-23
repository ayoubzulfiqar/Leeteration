class Solution:
    def shortestWordDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        pos1 = -1
        pos2 = -1
        min_dist = float('inf')

        for i, current_word in enumerate(wordsDict):
            if current_word == word1:
                if word1 == word2:
                    if pos1 != -1:
                        min_dist = min(min_dist, i - pos1)
                    pos1 = i
                else:
                    pos1 = i
                    if pos2 != -1:
                        min_dist = min(min_dist, abs(pos1 - pos2))
            elif current_word == word2:
                pos2 = i
                if pos1 != -1:
                    min_dist = min(min_dist, abs(pos1 - pos2))
        
        return min_dist