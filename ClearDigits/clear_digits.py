class Solution:
    def clearDigits(self, s: str) -> str:
        char_list = list(s)

        while True:
            first_digit_idx = -1
            
            for i in range(len(char_list)):
                if char_list[i].isdigit():
                    first_digit_idx = i
                    break
            
            if first_digit_idx == -1:
                break
            
            non_digit_idx = -1
            for j in range(first_digit_idx - 1, -1, -1):
                if not char_list[j].isdigit():
                    non_digit_idx = j
                    break
            
            del char_list[first_digit_idx]
            del char_list[non_digit_idx]
            
        return "".join(char_list)