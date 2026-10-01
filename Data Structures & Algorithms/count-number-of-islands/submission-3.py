class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        columns = len(grid[0])
        visit = set()
        islands = 0

        if not grid:
            return 0

        def dfs(r,c):
            stack = []
            visit.add((r,c))
            stack.append((r,c))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            while stack:
                row, col = stack.pop()
                for dr, dc in directions:
                    nr = row+dr
                    nc = col+dc
                    if (nr in range(rows) and nc in range(columns) and grid[nr][nc] == "1" and (nr,nc) not in visit):
                        visit.add((nr,nc))
                        stack.append((nr,nc))


        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r,c)
                    islands += 1
        return islands
        