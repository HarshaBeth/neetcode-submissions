class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(x, n):
            if n == 0: return 1
            if x == 0: return 0
            

            res = helper(x * x, n // 2) # e.g. x^6 = (x^2)^3
            return res * x if n % 2 else res # e.g. x^5 = (x^2)^2 * x
        
        # Account for negative numbers too!!!
        res = helper(x, abs(n))
        return res if n >= 0 else 1/res