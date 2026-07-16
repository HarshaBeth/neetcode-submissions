class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False
        
        # Create adjacency map
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        

        # Build DFS function (we need to keep track of the PREVIOUS node, sice there's undirectional edges)
        visit = set()
        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)
            for j in adj[node]:
                if j == prev: continue
                if not dfs(j, node): return False
            
            return True
        
        # Complete (no need for loop, just start with a node 0)
        return dfs(0, -1) and n == len(visit)