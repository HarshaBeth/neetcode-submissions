class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        # Creating adjacency map and checking invalid prefix
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))

            # Check invalid prefix
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break # break after the first difference, the later don't matter
        

        # Creating DFS
        visit = {} # False = already visited and good to go, True = this is a loop (invalid)
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True
            
            for nei in adj[c]:
                if dfs(nei):
                    return True

            visit[c] = False
            res.append(c)
        
        # Now check if the adjacency map is correct
        for c in adj:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)






