class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        pair_count = 0
        seen_words = set()

        for word in words:
            reversed_word = word[::-1]
            if reversed_word in seen_words:
                pair_count += 1
                seen_words.remove(reversed_word)
            else:
                seen_words.add(word)
        
        return pair_count