class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x - 1]:
                continue

            for i in range(x+1,len(nums)):
                # Skip duplicate first elements
                if i > x+1 and nums[i] == nums[i - 1]:
                    continue

                j = i + 1
                k = len(nums) - 1

                while j < k:
                    total = nums[x] + nums[i] + nums[j] + nums[k]

                    if total == target:
                        if sorted([nums[x], nums[i], nums[j], nums[k]]) not in ans:
                            ans.append([nums[x], nums[i], nums[j], nums[k]])

                        j += 1
                        k -= 1

                        # Skip duplicates for j
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1

                        # Skip duplicates for k
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1

                    elif total < target:
                        j += 1

                    else:
                        k -= 1

        return ans