class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        all_caps = word.isupper()
        all_lower = word.islower()
        first_cap_rest_lower = word[0].isupper() and word[1:].islower()
        
        return all_caps or all_lower or first_cap_rest_lower