class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {} # stores the last index of each character

        for i, c in enumerate(s):
            lastIndex[c] = i
        
        # Now start the loop to store the sizes
        res = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1            
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0
        
        return res