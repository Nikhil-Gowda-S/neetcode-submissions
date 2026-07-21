class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,v in enumerate(numbers):
            rem=target-v
            if rem in numbers:
                idx2=numbers.index(rem)
                if i!=idx2:
                    return [i+1,idx2+1]
        """def twoSum(numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1   # Need a larger sum, move left pointer right
        else:
            right -= 1  # Need a smaller sum, move right pointer left
"""