class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # To solve this type of problem, we use UnionFind Algorithm

        parent = [i for i in range(n)]
        rank = [1] * n

        def findParent(node): # This function only exists because of union function
            res = node

            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        
        def union(n1, n2): # this is where the merging is happening, in the union function
            parent1, parent2 = findParent(n1), findParent(n2)

            if parent1 == parent2:
                return 0
            
            if rank[parent2] > rank[parent1]:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            else:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            
            return 1


        groups = n
        for n1, n2 in edges:
            groups -= union(n1, n2)
        
        return groups



        