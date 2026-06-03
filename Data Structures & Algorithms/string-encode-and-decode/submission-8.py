class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs)):
            res += (str(len(strs[i])) + '#')
            res += strs[i]
        
        return res

    def decode(self, s: str) -> List[str]:
        res_list = []
        i = 0
        
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
               
            length = int(s[i:j])

            word_start = j+1
            word_end = word_start+length

            res_list.append(s[word_start: word_end])

            i = word_end
        
        return res_list
            
