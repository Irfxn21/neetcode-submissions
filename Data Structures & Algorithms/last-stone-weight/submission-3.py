class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:

            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            if second<first:
                diff = first - second
                heapq.heappush(heap, -diff)
        
        heap.append(0)
        return abs(heap[0])





        