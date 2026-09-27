class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        ops = {"+", "-", "*", "/"}

        calc = 0

        for i in tokens:

            if i in ops:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if i == "+":
                    calc = num2 + num1
                elif i == "-":
                    calc = num2 - num1
                elif i == "*":
                    calc = num2 * num1
                elif i == "/":
                    calc = num2 / num1
                stack.append(calc)
            else:
                stack.append(i)
        
        return int(stack[0])


        