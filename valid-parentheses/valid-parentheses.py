class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair = {}
        pair[")"] = "("
        pair["}"] = "{"
        pair["]"] = "["

        if len(s)%2 != 0:
            return False

        q = []
        for i in s:
            if i not in pair:
                q.append(i)
            elif q:
                if pair[i] != q[-1]:
                    return False
                q.pop()
            else:
                return False
        return not q
