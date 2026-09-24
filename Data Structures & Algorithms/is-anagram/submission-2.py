class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        word1 = {}
        word2 = {}

        for i in s:
            if i == ' ':
                continue
            if i in word1:
                word1[i] += 1
            else:
                word1[i] = 1
        
        for i in t:
            if i == ' ':
                continue
            if i in word2:
                word2[i] += 1
            else:
                word2[i] = 1

        if word1 == word2:
            return True
        else:
            return False

        