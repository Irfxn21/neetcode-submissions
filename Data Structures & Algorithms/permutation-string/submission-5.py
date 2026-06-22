class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l = 0
        curr = 0
        h1 = {}
        h2 = {}

        for i in range(len(s1)):
            if s1[i] in h1:
                h1[s1[i]] += 1
            else:
                h1[s1[i]] = 1


        for r in range(len(s2)):

            if s2[r] in h2:
                h2[s2[r]] += 1
            else:
                h2[s2[r]] = 1

            while (s2[l] not in h1 or (r-l+1)>len(s1)) and l != r:

                if h2[s2[l]] == 1:
                    h2.pop(s2[l])
                else:
                    h2[s2[l]] -= 1
                l += 1
                

            if h1 == h2:
                return True

        
        return False