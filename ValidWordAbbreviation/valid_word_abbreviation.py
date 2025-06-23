```python
class Solution:
    def isValidWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0  # Pointer for word
        j = 0  # Pointer for abbr

        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                # If the current character in abbr is a digit
                # Handle leading zero: '0' alone or '0' followed by another digit is invalid.
                # A single '0' is not a valid abbreviation for 0 characters.
                if abbr[j] == '0':
                    return False
                
                num = 0
                # Parse the complete number from abbr
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                
                # Advance the word pointer by the parsed number
                i += num
            else:
                # If the current character in abbr is a letter
                # Check for character match
                if word[i] == abbr[j]:
                    i += 1
                    j += 1
                else:
                    # Mismatch found
                    return False
        
        # After the loop, both pointers must have reached the end of their respective strings
        # for the abbreviation to be valid.
        return i == len(word) and j == len(abbr)

```