class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # FIRST SOLITION
        # res = 0

        # while n: # Meaning when it is not 0
        #     res += n % 2
        #     n = n >> 1 # Bit shift
        
        # return res

        # SECOND SOLUTION
        res = 0

        while n:
            n &= (n-1)
            res += 1
        
        return res