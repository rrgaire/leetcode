"""
210. Course Schedule II
Solved
Medium
Topics
Companies
Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.


"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        res = list()
        hashdict = {i: [] for i in range(numCourses)}
        cycle = set()
        visited = set()

        for c, p in prerequisites:
            hashdict[c].append(p)

        def dfs(c):
            if c in cycle:
                return False
            if c in visited:
                return True
            
            cycle.add(c)
            for p in hashdict[c]:
                if not dfs(p):
                    return False
            
            cycle.remove(c)
            visited.add(c)
            res.append(c)
            return True


        # def dfs(c):
        #     if c in visited:
        #         return False
            
        #     if hashdict[c] == []:
        #         if c not in res:
        #             res.append(c)
        #         return True 
            
        #     visited.add(c)
        #     for pre in hashdict[c]:
        #         if not dfs(pre):
        #             return False

        #     visited.remove(c)
        #     hashdict[c] = []
        #     res.append(c)
        #     return True

        
        


        for i in range(numCourses):
            if not dfs(i):
                return []

        return res
            

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)
        
        def dfs(i, res):
            if i in visited:
                return visited[i]
            
            visited[i] = False
            for n in adj[i]:
                if not dfs(n, res):
                    return visited[i]
            
            visited[i] = True
            res.append(i)
            return visited[i]
        
        res = []
        visited = {}
        for i in range(numCourses):
            if not dfs(i, res):
                return []
        
        return res

        