import math

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7

        def is_prime(num: int) -> bool:
            if num <= 1:
                return False
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True

        primes_count = 0
        for i in range(1, n + 1):
            if is_prime(i):
                primes_count += 1

        non_primes_count = n - primes_count

        def calculate_factorial(k: int) -> int:
            res = 1
            for i in range(1, k + 1):
                res = (res * i) % MOD
            return res

        ans = (calculate_factorial(primes_count) * calculate_factorial(non_primes_count)) % MOD
        return ans