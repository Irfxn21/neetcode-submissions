class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        maxArea = 0

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))
            area = 1
            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            while q:
                rw, cl = q.popleft()
                for dr, dc in directions:
                    nr = rw+dr
                    nc = cl+dc

                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr,nc) not in visit):
                        area += 1
                        q.append((nr,nc))
                        visit.add((nr,nc))
            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    maxArea = max(maxArea, bfs(r,c))

        return maxArea
        