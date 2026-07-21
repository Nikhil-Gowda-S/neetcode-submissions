class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):
            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    ans.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # Skip duplicates for j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicates for k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif total < 0:
                    j += 1

                else:
                    k -= 1

        return ans