class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        letters = set()
        curr = 0
        length = 0

        for r in range(len(s)):

            while s[r] in letters and l != r:
                letters.remove(s[l])
                l += 1
            
            letters.add(s[r])
            curr = r - l + 1
            length = max(length, curr)
        
        return length
    

            



        