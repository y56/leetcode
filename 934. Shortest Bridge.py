class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
# ref:
# https://leetcode.com/problems/shortest-bridge/discuss/189293/C%2B%2B-BFS-Island-Expansion-%2B-UF-Bonus
        R,C=len(A),len(A[0])
        def inside(i,j):
            return 0<=i<R and 0<=j<C
        def dfs_paint_2(i,j):
            A[i][j]=2
            for (ii,jj) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if inside(ii,jj) and A[ii][jj]==1:
                    dfs_paint_2(ii,jj)
        def neighbor_is_1(i,j):
            for (ii,jj) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if inside(ii,jj) and A[ii][jj]==1:
                    return True
            return False
        def paint_neighbor(i,j,color):
            for (ii,jj) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if inside(ii,jj) and A[ii][jj]==0:
                    A[ii][jj]=color       
        def paint_2():
            for i,row in enumerate(A):
                for j,ele in enumerate(row):
                    if ele==1:
                        dfs_paint_2(i,j)
                        return
        paint_2()
        # now the island I have touched is in color-2
        # the other one, untouched, is in color-1
        for color in range(2,max(R,C)+2):
            for i,row in enumerate(A):
                for j,ele in enumerate(row):
                    if ele==color:
                        if neighbor_is_1(i,j):
                            return color-2
                        paint_neighbor(i,j,color+1)
        # time: edge^3
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
# ref:
# https://leetcode.com/problems/shortest-bridge/discuss/189293/C%2B%2B-BFS-Island-Expansion-%2B-UF-Bonus
        R,C=len(A),len(A[0])
        def inside(i,j):
            return 0<=i<R and 0<=j<C
        island2=collections.deque()
        def dfs_paint_2(i,j):
            A[i][j]=2
            island2.append((i,j))
            for (ii,jj) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if inside(ii,jj) and A[ii][jj]==1:
                    dfs_paint_2(ii,jj)    
        def paint_2():
            for i,row in enumerate(A):
                for j,ele in enumerate(row):
                    if ele==1:
                        dfs_paint_2(i,j)
                        return
        paint_2()
        # now the island I have touched is in color-2
        # the other one, untouched, is in color-1
        queue=island2
        while queue:
            i,j=queue.popleft()
            for (ii,jj) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if inside(ii,jj):
                    if A[ii][jj]==1:
                        return A[i][j]-2
                    if A[ii][jj]==0:
                        A[ii][jj]=A[i][j]+1 # paint color as puls 1
                        queue.append((ii,jj))

