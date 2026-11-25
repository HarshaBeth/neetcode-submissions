class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = [0] * 26

        for i in range(len(s)):
            letters[ord(s[i]) - ord('a')] += 1
        
        for j in range(len(t)):
            letters[ord(t[j]) - ord('a')] -= 1
        
        for count in letters:
            if count != 0:
                return False
        
        return True