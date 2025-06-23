class Solution:
    def similarRGB(self, color1: str, color2: str) -> bool:
        def simplify_component(hex_str: str) -> str:
            # Convert the 2-digit hexadecimal string to its decimal integer value.
            val = int(hex_str, 16)
            
            # The "simplified" RGB components are multiples of 17 (0x00, 0x11, ..., 0xFF).
            # To find the closest multiple of 17 to 'val', we divide 'val' by 17,
            # round to the nearest integer, and then multiply by 17.
            # Python's round() function rounds to the nearest even number for .5 cases,
            # which is an acceptable behavior for minimizing distance in this context.
            rounded_i = round(val / 17.0)
            simplified_val = int(rounded_i * 17)
            
            # Convert the simplified decimal value back to a 2-digit hexadecimal string.
            # hex() returns a string like '0xYY'. We slice [2:] to get 'YY'.
            # zfill(2) ensures the string is two characters long (e.g., '0' becomes '00').
            return hex(simplified_val)[2:].zfill(2)

        simplified_color1_parts = []
        simplified_color2_parts = []

        # Iterate through the R, G, B components of both colors.
        # Components are at indices 1-2 (R), 3-4 (G), 5-6 (B).
        for i in range(1, 7, 2):
            hex_component1 = color1[i : i+2]
            hex_component2 = color2[i : i+2]
            
            # Simplify each component and store it.
            simplified_color1_parts.append(simplify_component(hex_component1))
            simplified_color2_parts.append(simplify_component(hex_component2))
        
        # Reconstruct the simplified color strings.
        simplified_color1_str = "#" + "".join(simplified_color1_parts)
        simplified_color2_str = "#" + "".join(simplified_color2_parts)

        # Two colors are considered "similar" if their simplified versions are identical.
        return simplified_color1_str == simplified_color2_str