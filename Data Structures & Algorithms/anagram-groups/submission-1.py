class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        h = {}
        result = []

        for word in strs:
            order = "".join(sorted(word))

            if order in h:
                h[order].append(word)
            else:
                h[order] = []
                h[order].append(word)
        
        for i in h:
            result.append(h[i])
        
        return result

        