class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Make the adjacency map
        preMap = { i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        

        # The DFS method is to search for existing valid paths
        # If there is a CYCLE, return False
        output = []
        visit, cycle = set(), set() # visit means it is confirmed to be valid, cycle means it's the current cycle
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False
            
            cycle.remove(course)
            visit.add(course)
            output.append(course)

            return True
        
        # Run the loop across all courses
        for course in range(numCourses):
            if not dfs(course): return []
        
        return output

