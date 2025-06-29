class Solution:
    def reorderSpaces(self, text: str) -> str:
        total_spaces = text.count(' ')
        words = text.split()

        num_words = len(words)

        if num_words == 1:
            return words[0] + ' ' * total_spaces
        
        spaces_per_gap = total_spaces // (num_words - 1)
        extra_spaces = total_spaces % (num_words - 1)

        result = (spaces_per_gap * ' ').join(words)
        result += ' ' * extra_spaces

        return result