class Solution:
    def isValid(self, s: str) -> bool:
        
        h = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []

        for i in s:

            if stack and i in h and stack[-1] == h[i]:
                stack.pop()
            else:
                stack.append(i)
        
        return len(stack) == 0
                
