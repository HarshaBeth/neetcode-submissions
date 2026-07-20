class Solution:
    def longestPalindrome(self, s: str) -> str:
        # We start from the middle and expand outwards, that way we can get O(n^2) as our best solution
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd check
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
            
            # even check
            l, r = i, i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
        
        return res