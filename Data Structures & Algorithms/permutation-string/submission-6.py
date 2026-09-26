class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        h1 = {}
        h2 = {}

        l = 0

        for i in s1:
            if i in h1:
                h1[i] += 1
            else:
                h1[i] = 1
        
        for r in range(len(s2)):

            if s2[r] in h2:
                h2[s2[r]] += 1
            else:
                h2[s2[r]] = 1

            while (r-l+1) > len(s1) and l != r:
                if h2[s2[l]] == 1:
                    h2.pop(s2[l])
                else:
                    h2[s2[l]] -= 1
                
                l += 1

            print(h1)
            print(h2)
            if h1 == h2:
                return True
        
        return False
            
            
            


        