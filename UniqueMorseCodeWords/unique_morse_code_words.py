class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        transformations = set()
        
        for word in words:
            current_transformation_parts = []
            for char in word:
                # Calculate index for the morse_codes list (0 for 'a', 1 for 'b', etc.)
                index = ord(char) - ord('a')
                current_transformation_parts.append(morse_codes[index])
            
            # Join the parts to form the complete transformation string
            full_transformation = "".join(current_transformation_parts)
            transformations.add(full_transformation)
            
        return len(transformations)