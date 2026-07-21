class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)

            total = 0
            while n:
                d = n % 10
                total += d * d
                n //= 10

            n = total

        return True