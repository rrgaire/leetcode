"""
323. Count Connected Components
Solved 
There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

Return the total number of connected components in that graph.

Example 1:

Input:
n=3
edges=[[0,1], [0,2]]

Output:
1
Example 2:

Input:
n=6
edges=[[0,1], [1,2], [2,3], [4,5]]

Output:
2
Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2


"""

# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:

#         adj = {i: [] for i in range(n)}

#         for n1, n2 in edges:
#             adj[n1].append(n2)
#             adj[n2].append(n1)
        
#         visited = set()
#         count = 0

#         def dfs(node, cycle):
#             if node in cycle:
#                 return 
#             if adj[node] == []:
#                 visited.add(node)
#                 return
#             cycle.add(node)
#             visited.add(node)
#             for child in adj[node]:
#                 dfs(child, cycle)
#             adj[node] = []
            


#         for i in range(n):
#             if i not in visited:
#                 cycle = set()
#                 count += 1
#                 dfs(i, cycle)
        
#         return count


# Union Find Algorithm

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
        if p1 != p2:
            self.parent[p1] = p2 # we can use rank to decide which component is bigger
            return 1
        return 0
    
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unionfind = UnionFind()
        components = n
        for n1, n2 in edges:
            components -= unionfind.union(n1, n2)
        return components


        
        

        