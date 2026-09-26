class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        count = set()
        l = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in count and r != l:
                count.discard(s[l])
                l += 1
                
            
            count.add(s[r])
            curr = r - l + 1
            longest = max(longest, curr)
        return longest

        
        