class Solution:
    def toHexspeak(self, num: int) -> str:
        hex_representation = hex(num)[2:]
        
        hexspeak_result = []
        for char_digit in hex_representation:
            if char_digit == '0':
                hexspeak_result.append('O')
            elif char_digit == '1':
                hexspeak_result.append('I')
            elif '2' <= char_digit <= '9':
                return "ERROR"
            elif 'a' <= char_digit <= 'f':
                return "ERROR"
        
        return "".join(hexspeak_result)