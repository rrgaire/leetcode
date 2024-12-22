"""
1129. Shortest Path with Alternating Colors
Solved
Medium
Topics
Companies
Hint
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

 

Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]
 

Constraints:

1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < n

"""

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        red = {i: [] for i in range(n)}
        blue = {i: [] for i in range(n)}

        for src, dest in redEdges:
            red[src].append(dest)
        
        for src, dest in blueEdges:
            blue[src].append(dest)

        q = deque()
        q.append([0, 0, None])

        visit = set()
        visit.add((0, None))

        answer = [-1 for _ in range(n)]

        while q:

            node, length, color = q.popleft()

            if answer[node] == -1:
                answer[node] = length

            if color != 'RED':
                for nei in red[node]:
                    if (nei, 'RED') not in visit:
                        q.append([nei, length + 1, 'RED'])
                        visit.add((nei, 'RED'))
            
            if color != 'BLUE':
                for nei in blue[node]:
                    if (nei, 'BLUE') not in visit:
                        q.append([nei, length + 1, 'BLUE'])
                        visit.add((nei, 'BLUE'))
            
        return answer
        