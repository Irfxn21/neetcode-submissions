class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        h = {}
        result = []

        for i in strs:
            key = "".join(sorted(i))

            if key not in h:
                h[key] = []
            
            h[key].append(i)
        
        for j in h:
            result.append(h[j])

        return result