class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        char_rank = {}
        for i, char in enumerate(order):
            char_rank[char] = i

        def compare_words(word1, word2):
            len1, len2 = len(word1), len(word2)
            
            for i in range(min(len1, len2)):
                char1 = word1[i]
                char2 = word2[i]
                
                rank1 = char_rank[char1]
                rank2 = char_rank[char2]
                
                if rank1 < rank2:
                    return True
                elif rank1 > rank2:
                    return False
            
            return len1 <= len2

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            
            if not compare_words(word1, word2):
                return False
                
        return True