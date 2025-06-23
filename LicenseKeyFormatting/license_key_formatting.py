class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        cleaned_chars = []
        for char in s:
            if char != '-':
                cleaned_chars.append(char.upper())
        
        full_string = "".join(cleaned_chars)
        
        if not full_string:
            return ""

        formatted_parts = []
        current_group_chars = []
        
        for i in range(len(full_string) - 1, -1, -1):
            current_group_chars.append(full_string[i])
            
            if len(current_group_chars) == k:
                formatted_parts.append("".join(reversed(current_group_chars)))
                current_group_chars = []
        
        if current_group_chars:
            formatted_parts.append("".join(reversed(current_group_chars)))
            
        return "-".join(reversed(formatted_parts))