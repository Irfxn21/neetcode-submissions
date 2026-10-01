class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        heap = []
        h = {}
        result = []

        for i in range(len(nums)):
            if nums[i] in h:
                h[nums[i]] += 1
            else:
                h[nums[i]] = 1
        
        for i in h:
            heap.append((-h[i], i))
        
        heapq.heapify(heap)
        for i in range(k):
            count, num = heapq.heappop(heap)
            result.append(num)
        
        return result


        