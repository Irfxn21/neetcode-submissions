class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        h = {}
        g = {}

        for i in s:
            if i in g:
                g[i] += 1
            else:
                g[i] = 1
        
        for j in t:
            if j in h:
                h[j] += 1
            else:
                h[j] = 1
        
        return g == h
        