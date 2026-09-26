class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        curr = 0
        h = {}
        diff = 0
        longest = 0

        for r in range(len(s)):

            if s[r] in h:
                h[s[r]] += 1
            else:
                h[s[r]] = 1

            while (r-l+1)- max(h.values()) > k  and l != r:
                h[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest

            

        

        
        