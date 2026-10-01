class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        columns = len(grid[0])
        q = collections.deque()
        visit = set()
        fruit = 0
        count = 0
        

        

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))
                elif grid[r][c] == 1:
                    fruit += 1
        if fruit == 0:
            return fruit

        #directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def addRoom(r,c):
            if (r<0 or r == rows or c<0 or c == columns or (r,c) in visit or grid[r][c] == 0):
                return 0
            visit.add((r,c))
            q.append((r,c))
            return 1
        
        minute = -1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                fruit -= addRoom(r+1, c)
                fruit -= addRoom(r-1, c)
                fruit -= addRoom(r, c+1)
                fruit -= addRoom(r, c-1)
            minute += 1
        
        if fruit != 0:
            return -1
        else:
            return minute
            


        
        