class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        
        def calculate_height(r_available, b_available, start_color_is_red):
            needed_r = 0
            needed_b = 0
            current_height = 0
            k = 1
            while True:
                if start_color_is_red:
                    if k % 2 == 1: # Odd rows (1st, 3rd, ...) are the starting color (red)
                        needed_r += k
                    else: # Even rows (2nd, 4th, ...) are the other color (blue)
                        needed_b += k
                else: # Start color is blue
                    if k % 2 == 1: # Odd rows (1st, 3rd, ...) are the starting color (blue)
                        needed_b += k
                    else: # Even rows (2nd, 4th, ...) are the other color (red)
                        needed_r += k
                
                if needed_r <= r_available and needed_b <= b_available:
                    current_height = k
                    k += 1
                else:
                    break
            return current_height

        max_h = 0
        
        # Scenario 1: The first row is red
        max_h_red_start = calculate_height(red, blue, True)
        max_h = max(max_h, max_h_red_start)

        # Scenario 2: The first row is blue
        max_h_blue_start = calculate_height(red, blue, False)
        max_h = max(max_h, max_h_blue_start)
        
        return max_h