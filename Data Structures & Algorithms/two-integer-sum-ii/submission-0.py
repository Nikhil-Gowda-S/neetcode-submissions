class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,v in enumerate(numbers):
            rem=target-v
            if rem in numbers:
                idx2=numbers.index(rem)
                if i!=idx2:
                    return [i+1,idx2+1]
        