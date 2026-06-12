class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = {}, {}

        # Add all counts of characters from t
        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1

        # Initiate the 'have' and 'need' counts
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")

        # Start the two pointer process (make sure to keep track of the window)
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1
            
            # reduce the window while we have all the needs
            while have == need:
                if (r-l+1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                
                # remove the left character one by one
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l: r+1] if resLen != float("inf") else ""







