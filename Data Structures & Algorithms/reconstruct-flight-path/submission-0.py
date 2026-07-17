class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = { src: [] for src, dst in tickets}

        tickets.sort() # It is important to sort so that we will the answer in lexical order

        for src, dst in tickets:
            adj[src].append(dst)
        
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            
            temp = list(adj[src]) # Because we need this for looping since we will change the original
            for i, s in enumerate(temp):
                adj[src].pop(i)
                res.append(s)

                if dfs(s): return True

                adj[src].insert(i, s) # If this path is not good rn, then add it back and traverse back
                res.pop()
            return False
        
        dfs("JFK")
        return res

