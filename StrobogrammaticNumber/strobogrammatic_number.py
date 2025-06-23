class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapping = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        left = 0
        right = len(num) - 1

        while left <= right:
            char_left = num[left]
            char_right = num[right]

            if char_left not in mapping:
                return False
            
            if mapping[char_left] != char_right:
                return False
            
            left += 1
            right -= 1
        
        return True