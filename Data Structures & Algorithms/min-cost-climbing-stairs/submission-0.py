class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        one = 0   # dp[i+1]
        two = 0   # dp[i+2]

        for i in range(n - 1, -1, -1):
            curr = cost[i] + min(one, two)
            two = one
            one = curr

        return min(one, two)