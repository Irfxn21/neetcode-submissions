class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        h = {}
        q = {}
        result = []

        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        for i in h:
            if h[i] not in q:
                q[h[i]] = []
            q[h[i]].append(i)

        count = 0
        for i in range(len(nums),0, -1):
            if count == k:
                break
            if i in q:
                count += len(q[i])
                result.extend(q[i])

        return result



        