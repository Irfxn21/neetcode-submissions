class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows = len(grid)
        columns = len(grid[0])
        q = collections.deque()

        for r in range(rows):
            for c in range(columns):

                if grid[r][c] == 0:
                    q.append((r,c))
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        inf = 2147483647

        while q:
            row, col = q.popleft()
            
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if (r in range(rows) and c in range(columns) and grid[r][c] == inf):
                    grid[r][c] = grid[row][col] + 1
                    q.append((r,c))
        
        