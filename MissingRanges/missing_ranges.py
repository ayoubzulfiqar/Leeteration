class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[str]:
        
        def format_range(start, end):
            if start == end:
                return str(start)
            return f"{start}->{end}"

        result = []
        
        # Create an extended list with virtual boundaries
        # lower - 1 acts as the "previous" number before 'lower'
        # upper + 1 acts as the "next" number after 'upper'
        # This simplifies handling the ranges before the first number
        # and after the last number in nums.
        extended_nums = [lower - 1] + nums + [upper + 1]
        
        # Iterate through the extended list to find gaps
        for i in range(1, len(extended_nums)):
            # The start of the current number (or upper + 1)
            current_num_val = extended_nums[i]
            # The end of the previous number (or lower - 1)
            prev_num_val = extended_nums[i-1]
            
            # If there's a gap between the previous number and the current number
            # A gap exists if current_num_val is more than 1 greater than prev_num_val
            if current_num_val > prev_num_val + 1:
                missing_start = prev_num_val + 1
                missing_end = current_num_val - 1
                result.append(format_range(missing_start, missing_end))
                
        return result