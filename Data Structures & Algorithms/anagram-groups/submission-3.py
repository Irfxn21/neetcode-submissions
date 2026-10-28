class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        h = {}
        result = []

        for i in strs:
            word = ''.join(sorted(i))
            if word not in h:
                h[word] = []
            
            h[word].append(i)
        
        for j in h:
            result.append(h[j])
        
        return result


        