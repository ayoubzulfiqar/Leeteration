class Solution:
    def countTestedDevices(self, batteryPercentages: list[int]) -> int:
        n = len(batteryPercentages)
        tested_devices_count = 0

        for i in range(n):
            if batteryPercentages[i] > 0:
                tested_devices_count += 1
                for j in range(i + 1, n):
                    batteryPercentages[j] = max(0, batteryPercentages[j] - 1)
        
        return tested_devices_count