class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            remainder = columnNumber % 26
            if remainder == 0:
                result.append('Z')
                columnNumber = (columnNumber // 26) - 1
            else:
                result.append(chr(ord('A') + remainder - 1))
                columnNumber = columnNumber // 26
        return "".join(reversed(result))