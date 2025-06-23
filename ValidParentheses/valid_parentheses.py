class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:  # It's a closing bracket
                if not stack:  # No corresponding open bracket
                    return False
                top_element = stack.pop()
                if mapping[char] != top_element:
                    return False
            else:  # It's an opening bracket
                stack.append(char)

        return not stack  # True if stack is empty (all brackets matched), False otherwise