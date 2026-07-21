class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for _ in range(32):
            bit = n & 1          # get last bit
            result = (result << 1) | bit
            n >>= 1             # shift n to process next bit
        
        return result