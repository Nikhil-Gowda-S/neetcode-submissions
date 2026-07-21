"""class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def solve(idx, total, sub):
            if idx == len(candidates):
                if total == target:
                    temp = sorted(sub)
                    if temp not in res:
                        res.append(temp)
                return

            if total > target:
                return

            sub.append(candidates[idx])
            solve(idx + 1, total + candidates[idx], sub)
            sub.pop()

            solve(idx + 1, total, sub)

        solve(0, 0, [])
        return res"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start, target, sub):
            if target == 0:
                res.append(sub[:])
                return

            for i in range(start, len(candidates)):
                # Skip duplicate numbers
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since array is sorted, no need to continue
                if candidates[i] > target:
                    break

                sub.append(candidates[i])
                backtrack(i + 1, target - candidates[i], sub)
                sub.pop()

        backtrack(0, target, [])
        return res