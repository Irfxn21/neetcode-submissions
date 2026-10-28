class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        h = {}
        q = []
        result = []

        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        
        for i in h:
            q.append((-h[i], i))
        
        heapq.heapify(q)

        for i in range(k):
            count, val = heapq.heappop(q)
            result.append(val)
        
        return result


        




        