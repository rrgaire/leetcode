"""
2359. Find Closest Node to Given Two Nodes
Solved
Medium
Topics
Companies
Hint
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.

You are also given two integers node1 and node2.

Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.

Note that edges may contain cycles.

 

Example 1:


Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
Output: 2
Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.
Example 2:


Input: edges = [1,2,-1], node1 = 0, node2 = 2
Output: 2
Explanation: The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
The maximum of those two distances is 2. It can be proven that we cannot get a node with a smaller maximum distance than 2, so we return node 2.
 

Constraints:

n == edges.length
2 <= n <= 105
-1 <= edges[i] < n
edges[i] != i
0 <= node1, node2 < n


"""

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:


        adj = {}

        for i, e in enumerate(edges):
            adj[i] = e
        
        dist1 = {}
        dist2 = {}
        
        def bfs(q, dist):
            res = 0
            while q:
                res += 1
                for _ in range(len(q)):
                    n = q.popleft()

                    ne = adj[n]
                    if ne != -1:
                        if ne not in dist:
                            dist[ne] = res
                            q.append(ne)
            

        q = deque()
        q.append(node1)
        dist1[node1] = 0
        bfs(q, dist1)
        q = deque()
        q.append(node2)
        dist2[node2] = 0
        bfs(q, dist2)
        
        print(dist1, dist2)
        res = float('inf')
        ind = None
        for i in range(len(edges)):
            if i in dist1 and i in dist2:
                dist = max(dist1[i], dist2[i])
                if dist < res:
                    res = dist
                    ind = i

        return -1 if res == float('inf') else ind
        
