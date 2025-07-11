import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        sum_of_divisors = 1

        limit = int(math.sqrt(num))
        for i in range(2, limit + 1):
            if num % i == 0:
                sum_of_divisors += i
                if i * i != num:
                    sum_of_divisors += (num // i)
        
        return sum_of_divisors == num