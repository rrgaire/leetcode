"""
310. Minimum Height Trees
Solved
Medium
Topics
Companies
Hint
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

Example 1:


Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:


Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
 

Constraints:

1 <= n <= 2 * 104
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.


"""

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # adj = {i: [] for i in range(n)}

        # for a, b in edges:
        #     adj[a].append(b)
        #     adj[b].append(a)
        
        # def bfs(i, res):

        #     q = deque()
        #     q.append([i, 0])
        #     visit = set()
        #     visit.add(i)

        #     maxht = 0
        #     while q:
        #         n, ht = q.popleft()
        #         maxht = max(maxht, ht)

        #         for nei in adj[n]:
        #             if nei not in visit:
        #                 q.append([nei, ht + 1])
        #                 visit.add(nei)
        #     if maxht < res[0]:
        #         res[0] = maxht
        #         res[1] = [i]
        #     elif maxht == res[0]:
        #         res[1].append(i)
        #     return res
        
        # res = [n, []]
        # for i in range(n):
        #     res = bfs(i, res)
        
        # return res[1]


        if n == 1:
            return [0]
        
        adj = {i: [] for i in range(n)}
        indeg = [0] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indeg[u] += 1
            indeg[v] += 1
        
        q = deque()
        for i in range(n):
            if indeg[i] == 1:
                q.append(i)
        
        rem_nodes = n

        while rem_nodes > 2:
            rem_nodes -= len(q)
            for _ in range(len(q)):
                n = q.popleft()
                for nei in adj[n]:
                    indeg[nei] -= 1
                    if indeg[nei] == 1:
                        q.append(nei)
            
        return list(q)

        