class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # Mismatch found. Try deleting s[left] or s[right].
                # Option 1: Delete s[left] and check if the rest is a palindrome
                is_palindrome_after_deleting_left = self._is_palindrome_range(s, left + 1, right)

                # Option 2: Delete s[right] and check if the rest is a palindrome
                is_palindrome_after_deleting_right = self._is_palindrome_range(s, left, right - 1)

                return is_palindrome_after_deleting_left or is_palindrome_after_deleting_right
            
            left += 1
            right -= 1
        
        # If the loop completes, the string is already a palindrome
        return True

    def _is_palindrome_range(self, s: str, left: int, right: int) -> bool:
        """
        Helper function to check if a substring defined by [left, right] indices is a palindrome.
        """
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True