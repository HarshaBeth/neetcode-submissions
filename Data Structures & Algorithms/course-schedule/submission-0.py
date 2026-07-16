class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # So think of this as bunch of nodes (connected or disconnected)
        # Thereofre, DFS would be suitable to solve this question

        preMap = { i: [] for i in range(numCourses) }
        for course, prereq in prerequisites: # append all prerequisites for each course
            preMap[course].append(prereq)
        
        # Now begin dfs (write dfs function)
        visit = set()
        def dfs(course):
            if course in visit:
                return False
            if preMap[course] == []:
                return True

            visit.add(course)
            for crs in preMap[course]: # e.g. course -> [3, 4, 5]
                if not dfs(crs): return False
            visit.remove(course)
            preMap[course] = [] # remove all visited nodes since they returned True and so we don't 
                                # go through them again and waste time/computation

            return True
        
        for course in range(numCourses):
            if not dfs(course): return False
        return True