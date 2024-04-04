class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for c in tokens:
            if c not in "+-*/":
                stack.append(int(c))
            else:
                a = stack.pop()
                b = stack.pop()
                if c == "+":
                    stack.append(b + a)
                elif c == "-":
                    stack.append(b - a)
                elif c == "*":
                    stack.append(b * a)
                elif c == "/":
                    stack.append(int(float(b)/a))
        return stack[-1]