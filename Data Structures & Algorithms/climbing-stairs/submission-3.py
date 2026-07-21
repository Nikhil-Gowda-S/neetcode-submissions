class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)

        def solve(n):
            if n == 0 or n == 1:
                return 1

            if dp[n] != -1:
                return dp[n]

            dp[n] = solve(n - 1) + solve(n - 2)
            return dp[n]

        return solve(n)