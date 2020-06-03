"""
There are n cities numbered from 0 to n-1 and n-1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [a, b] represents a road from city a to b.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach the city 0 after reorder.

 

Example 1:

Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 2:

Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 3:

Input: n = 3, connections = [[1,0],[2,0]]
Output: 0

 

Constraints:

    2 <= n <= 5 * 10^4
    connections.length == n-1
    connections[i].length == 2
    0 <= connections[i][0], connections[i][1] <= n-1
    connections[i][0] != connections[i][1]


"""
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.ans=0
        visited=set()
        those_to  =collections.defaultdict(list)
        those_from=collections.defaultdict(list)
        for a,b in connections:
            those_to[b].append(a) # b is from a 
            those_from[a].append(b) # from a to b
        bfs_q = collections.deque([0])
        while bfs_q:
            n = bfs_q[0]
            visited.add(n)
            bfs_q.popleft()
            for e in those_to[n]: # no need to reorder
                if e not in visited:
                    bfs_q.append(e)
            for e in those_from[n]: # need to reorder
                if e not in visited:
                    bfs_q.append(e)
                    self.ans+=1
        return self.ans                   
