from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operators = ("+", "-", "/", "*")
        for token in tokens:

            if token not in operators:
                stack.insert(0, int(token))
                continue

            first = stack.pop(0)
            second = stack.pop(0)
            
            if token == "+":
                stack.insert(0, first + second)
            elif token == "*":
                stack.insert(0, first * second)
            elif token == "/":
                stack.insert(0, int(second/first))
            elif token == "-":
                stack.insert(0, second-first)
        return stack[0]


if __name__ == '__main__':
    sol = Solution()
    tokens = ["4","3","-"]
    sol.evalRPN(tokens=tokens)