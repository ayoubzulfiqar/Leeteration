class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        lines = 1
        current_line_width = 0
        
        for char in s:
            char_width = widths[ord(char) - ord('a')]
            
            if current_line_width + char_width > 100:
                lines += 1
                current_line_width = char_width
            else:
                current_line_width += char_width
                
        return [lines, current_line_width]