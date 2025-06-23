class Solution:
    def isConfusingNumber(self, n: int) -> bool:
        rotations = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        s = str(n)
        rotated_digits_list = []

        for char_digit in s:
            if char_digit not in rotations:
                return False
            rotated_digits_list.append(rotations[char_digit])

        # To get the 180-degree rotated number,
        # we first get the rotated version of each digit,
        # and then reverse the order of these rotated digits.
        # For example, if n = 68:
        # '6' rotates to '9'
        # '8' rotates to '8'
        # rotated_digits_list becomes ['9', '8']
        # Reversing this list gives ['8', '9'], which forms the number 89.
        rotated_val_str = "".join(rotated_digits_list[::-1])
        
        rotated_val = int(rotated_val_str)

        return n != rotated_val