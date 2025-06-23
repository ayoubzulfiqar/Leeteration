import collections

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        words1 = s1.split()
        words2 = s2.split()
        
        all_words = words1 + words2
        
        word_counts = collections.Counter(all_words)
        
        uncommon_words = []
        for word, count in word_counts.items():
            if count == 1:
                uncommon_words.append(word)
                
        return uncommon_words