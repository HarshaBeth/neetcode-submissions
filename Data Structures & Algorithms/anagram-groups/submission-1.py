class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list) # key: tuple, value: list
        
        for word in strs:

            letters = [0] * 26
            for w in word:
                letters[ord(w) - ord('a')] += 1
            
            anagrams[tuple(letters)].append(word)
        
        return list(anagrams.values())