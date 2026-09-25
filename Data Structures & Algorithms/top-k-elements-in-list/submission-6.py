class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        h = {}
        countSet = set()
        resultSet = set()
        result = []

        for i in nums:
            countSet.add(i)

            if i in h:
                h[i] += 1
            else:
                h[i] = 1
            
        
        for i in range(k):
            mostFreq = 0
            count = 0 
            if not countSet:
                break
            for j in countSet:
                if h[j] >= count:
                    count = h[j]
                    mostFreq = j
            result.append(mostFreq)
            countSet.discard(mostFreq)

        return result


        