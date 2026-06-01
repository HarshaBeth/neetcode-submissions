from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_lists = defaultdict(list)

        for word in (strs):
            unique_count = [0] * 26

            for char in word:
                unique_count[ord(char) - ord('a')] += 1
            
            anagram_lists[tuple(unique_count)].append(word)

        return list(anagram_lists.values())