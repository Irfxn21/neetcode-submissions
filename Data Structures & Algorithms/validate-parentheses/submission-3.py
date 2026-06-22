class Solution:
    def isValid(self, s: str) -> bool:

        s1 = []

        for i in s:
            if i == ")":
                if len(s1) == 0 or s1[-1] != "(":
                    return False
                else:
                    s1.pop()
            elif i == "}":
                if len(s1) == 0 or s1[-1] != "{":
                    return False
                else:
                    s1.pop()
            elif i == "]":
                if len(s1) == 0 or s1[-1] != "[":
                    return False
                else:
                    s1.pop()
            else:
                s1.append(i)

            
        return len(s1) == 0
        