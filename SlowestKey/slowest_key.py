class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        n = len(releaseTimes)

        max_duration = releaseTimes[0]
        result_key = keysPressed[0]

        prev_release_time = releaseTimes[0]

        for i in range(1, n):
            current_duration = releaseTimes[i] - prev_release_time
            current_key = keysPressed[i]

            if current_duration > max_duration:
                max_duration = current_duration
                result_key = current_key
            elif current_duration == max_duration:
                if current_key > result_key:
                    result_key = current_key
            
            prev_release_time = releaseTimes[i]
        
        return result_key