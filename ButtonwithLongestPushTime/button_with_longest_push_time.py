class Solution:
    def longestPushTime(self, events: list[list[int]]) -> int:
        max_duration = 0
        result_index = -1
        previous_time = 0

        for index, time in events:
            current_duration = time - previous_time

            if current_duration > max_duration:
                max_duration = current_duration
                result_index = index
            elif current_duration == max_duration:
                result_index = min(result_index, index)
            
            previous_time = time
        
        return result_index