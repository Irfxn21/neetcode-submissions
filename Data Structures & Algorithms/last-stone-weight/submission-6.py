class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if not stones:
            return 0
        
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            diff = first - second

            if diff != 0:
                heapq.heappush(stones, -diff)
        
        if stones:
            return -stones[0]
        else:
            return 0


        