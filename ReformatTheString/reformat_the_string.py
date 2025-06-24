class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        digits = []

        for char in s:
            if char.isdigit():
                digits.append(char)
            else:
                letters.append(char)

        len_letters = len(letters)
        len_digits = len(digits)

        if abs(len_letters - len_digits) > 1:
            return ""

        result = []
        
        if len_letters >= len_digits:
            first_list = letters
            second_list = digits
        else:
            first_list = digits
            second_list = letters
        
        for i in range(len(second_list)):
            result.append(first_list[i])
            result.append(second_list[i])
        
        if len(first_list) > len(second_list):
            result.append(first_list[-1])
            
        return "".join(result)