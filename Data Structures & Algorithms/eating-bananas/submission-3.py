class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        high = max(piles)

        l = 1
        r = high-1
        k = high
        

        while l<=r:
            mid = (l+r)//2
            total = 0

            for i in piles:
                total += math.ceil(i/mid)
            
            if total <= h:
                k = min(k, mid)
                r = mid-1
            else:
                l = mid+1
        return k
        