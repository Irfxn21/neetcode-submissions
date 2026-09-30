from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        rows = len(grid)
        columns = len(grid[0])
        islands = 0
        visit  = set()

        def bfs(r,c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows) and c in range(columns) and grid[r][c] == "1" and (r,c) not in visit):
                        visit.add((r,c))
                        q.append((r,c))

        for r in range(rows):
            for c in range(columns):

                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1

        return islands