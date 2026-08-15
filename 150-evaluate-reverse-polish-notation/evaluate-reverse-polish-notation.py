class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch in ['+','-','*','/']:
                num1 = stack.pop()
                num2 = stack.pop()

                if ch == '+':
                    stack.append(num1+num2)
                elif ch == '-':
                    stack.append(num2-num1)
                elif ch =='*':
                    stack.append(num1*num2)
                elif ch =='/':
                    stack.append(int(num2/num1))
            else:
                stack.append(int(ch))

            
        return stack[0]