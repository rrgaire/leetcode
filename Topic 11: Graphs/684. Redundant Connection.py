"""
684. Redundant Connection
Solved
Medium
Topics
Companies
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.

"""

class UnionFind:
    def __init__(self):
        self.parent = {}

    def findParent(self, node):
        y = self.parent.get(node, node)
        if y != node:
            self.parent[node] = self.findParent(y)
            y = self.parent[node]
        return y

    def union(self, n1, n2):
        p1 = self.findParent(n1)
        p2 = self.findParent(n2)
        self.parent[p1] = p2

        if p1 == p2:
            return True
        return False
        


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind()

        for n1, n2 in edges:
            if uf.union(n1, n2):
                return [n1, n2]



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        par = [i for i in range(n)]


        def findParent(node):
            y = node
            while y != par[y]:
                par[y] = par[par[y]]
                y = par[y]
            return y
        
        for n1, n2 in edges:
            p1 = findParent(n1 - 1)
            p2 = findParent(n2 - 1)

            if p1 == p2:
                return [n1, n2]
            
            else:
                par[p1] = p2
        
