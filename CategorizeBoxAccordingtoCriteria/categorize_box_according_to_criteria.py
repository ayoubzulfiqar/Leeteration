class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        
        is_bulky = False
        is_heavy = False

        # Check for Bulky criteria
        # Any dimension >= 10^4
        if length >= 10000 or width >= 10000 or height >= 10000:
            is_bulky = True
        
        # Volume >= 10^9
        volume = length * width * height
        if volume >= 1000000000:
            is_bulky = True
        
        # Check for Heavy criteria
        # Mass >= 100
        if mass >= 100:
            is_heavy = True
            
        # Determine the final category based on both flags
        if is_bulky and is_heavy:
            return "Both"
        elif is_bulky and not is_heavy:
            return "Bulky"
        elif not is_bulky and is_heavy:
            return "Heavy"
        else: # not is_bulky and not is_heavy
            return "Neither"