class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if s == goal:
            return True

        # If goal is a rotation of s, then goal must be a substring of s + s.
        # For example, if s = "abcde", then s + s = "abcdeabcde".
        # Any rotation of s, like "cdeab", will be found within "abcdeabcde".
        return goal in (s + s)