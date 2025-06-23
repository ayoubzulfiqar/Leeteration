class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        char_list = list(s)
        left = 0
        right = len(char_list) - 1

        while left < right:
            while left < right and not char_list[left].isalpha():
                left += 1
            while left < right and not char_list[right].isalpha():
                right -= 1

            if left < right:
                char_list[left], char_list[right] = char_list[right], char_list[left]
                left += 1
                right -= 1
        
        return "".join(char_list)