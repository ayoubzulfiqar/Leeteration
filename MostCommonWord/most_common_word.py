import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        banned_set = set(banned)
        
        paragraph_lower = paragraph.lower()
        
        punctuation_to_replace = "!?',;."
        for punc in punctuation_to_replace:
            paragraph_lower = paragraph_lower.replace(punc, " ")
            
        words = paragraph_lower.split()

        word_counts = collections.Counter()
        for word in words:
            if word not in banned_set:
                word_counts[word] += 1
        
        most_frequent_word = ""
        max_count = 0
        
        for word, count in word_counts.items():
            if count > max_count:
                max_count = count
                most_frequent_word = word
                
        return most_frequent_word