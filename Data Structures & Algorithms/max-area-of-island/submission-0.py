class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        columns = len(grid[0])
        visit = set()
        max_area = 0

        if not grid:
            return 0
        
        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            a = 1

            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows) and c in range(columns) and grid[r][c] == 1 and (r,c) not in visit):
                        a += 1
                        visit.add((r,c))
                        q.append((r,c))
            return a

        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (r,c) not in visit:
                    area = bfs(r,c)
                    max_area = max(max_area, area)
        
        return max_area