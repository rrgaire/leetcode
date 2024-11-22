"""

997. Find the Town Judge
Solved
Easy
Topics
Companies
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
 

Constraints:

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n

"""

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        # time: O(V + E) | space: O(V)
        poss = set([i for i in range(1, n + 1)])
        count = {}
        for i in range(1, n + 1):
            count[i] = set([j for j in range(1, n + 1) if i != j])
        
        for a, b in trust:
            if a in poss:
                poss.remove(a)
            count[b].remove(a)
        
        for k, v in count.items():
            if k in poss and not v:
                return k
        return -1

        # time: O(V + E) | space: O(V)
        incoming = {i: 0 for i in range(1, n + 1)}
        outgoing = {i: 0 for i in range(1, n + 1)}

        for e1, e2 in trust:
            outgoing[e1] += 1
            incoming[e2] += 1
        
        for i in range(1, n + 1):
            if incoming[i] == n - 1 and outgoing[i] == 0:
                return i
        return -1
        
