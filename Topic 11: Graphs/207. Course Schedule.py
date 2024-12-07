"""
207. Course Schedule
Solved
Medium
Topics
Companies
Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # time: O(n.p) | space: O(n.p)
        preMap = {i: [] for i in range(numCourses)}

        for c, p in prerequisites:
            preMap[c].append(p)
        visited = set()

        def dfs(c):
            if c in visited:
                return False

            if preMap[c] == []:
                return True

            visited.add(c)
            for course in preMap[c]:

                if not dfs(course):
                    return False
            preMap[c] = []
            visited.remove(c) 
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True    
    

    class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)

        courses = {}


        def dfs(i):
            if i in courses:
                return courses[i]
            
            courses[i] = False
            for n in adj[i]:
                if not dfs(n):
                    courses[i] = False
                    return False
            
            courses[i] = True
            return True



        res = True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        
        