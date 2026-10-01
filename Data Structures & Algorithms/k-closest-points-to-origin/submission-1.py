class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        h = {}
        heap=[]
        result = []

        for i in range(len(points)):
            calc = ((points[i][0]**2) + (points[i][1]**2))
            heap.append((calc, points[i][0], points[i][1]))
            
        
        heapq.heapify(heap)

        for i in range(k):
            distance, x, y = heapq.heappop(heap)
            result.append([x,y])
        
        return result

            
        
        