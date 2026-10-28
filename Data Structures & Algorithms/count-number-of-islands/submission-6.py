class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        islands = 0

        def dfs(r,c):
            stack = []
            stack.append((r,c))
            visit.add((r,c))
            directions = [[0,1], [0,-1], [1,0], [-1,0]]

            while stack:
                rw, cl = stack.pop()
                for dr, dc in directions:
                    nr = rw + dr
                    nc = cl + dc

                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1" and (nr,nc) not in visit):
                        stack.append((nr, nc))
                        visit.add((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r, c)
                    islands += 1
        
        return islands
        