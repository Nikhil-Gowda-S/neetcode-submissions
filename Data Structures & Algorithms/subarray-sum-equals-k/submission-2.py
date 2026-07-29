class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0

        freq = {}
        freq[0] = 1

        for num in nums:
            prefix_sum += num

            count += freq.get(prefix_sum - k, 0)

            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return count

"""from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum=0
        freq=defaultdict(int)
        freq[0]=1
        count=0
        for num in nums:
            prefixsum+=num
            count+=freq[prefixsum-k]
            freq[prefixsum]+=1
        return count






        count=0
        for i in range(len(nums)):
            total=nums[i]
            if total==k:
                count+=1
            for j in range(i+1,len(nums)):
                total+=nums[j]
                if total==k:
                    count+=1
        return count"""
        