class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {")":"(",    "}":"{",   "]":"["}
        stack = []
        for c in s:
            if c not in bracket_map:
                stack.append(c)
                continue
            elif stack != [] and bracket_map.get(c) == stack[-1]:
                stack.pop()
            else:
                return False
        if stack != []: return False
        return True