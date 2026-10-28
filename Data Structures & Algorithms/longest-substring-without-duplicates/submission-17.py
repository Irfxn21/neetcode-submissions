class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        count = set()
        longest = 0

        for r in range(len(s)):

            while s[r] in count and l != r:
                count.remove(s[l])
                l += 1
            
            count.add(s[r])
            longest = max(longest, r-l+1)
        
        return longest
        