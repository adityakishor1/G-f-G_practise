from typing import List

class Solution:
    def getPrimes(self, n: int) -> List[int]:
        def sieve_of_eratosthenes(num: int) -> List[bool]:
            primes = [True] * (num + 1)
            primes[0] = primes[1] = False
            p = 2
            while p ** 2 <= num:
                if primes[p]:
                    for i in range(p ** 2, num + 1, p):
                        primes[i] = False
                p += 1
            return primes

        primes = sieve_of_eratosthenes(n)
        for i in range(2, n):
            if primes[i] and primes[n - i]:
                return [i, n - i]
        return [-1, -1]
