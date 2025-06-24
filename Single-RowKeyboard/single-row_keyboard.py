class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        char_to_index = {}
        for i, char in enumerate(keyboard):
            char_to_index[char] = i

        total_time = 0
        prev_index = 0  # Starting position on the keyboard is always index 0

        for char in word:
            current_index = char_to_index[char]
            total_time += abs(current_index - prev_index)
            prev_index = current_index
            
        return total_time