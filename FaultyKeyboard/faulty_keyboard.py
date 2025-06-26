class Solution:
    def finalString(self, s: str) -> str:
        screen_content = []
        for char in s:
            if char == 'i':
                screen_content.reverse()
            else:
                screen_content.append(char)
        return "".join(screen_content)