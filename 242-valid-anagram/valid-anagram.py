class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        
        s_set = defaultdict(int)

        for i in s:
            s_set[i] += 1
        
        for i in t:
            if i not in s_set or s_set[i]<=0:
                return False
            else:
                s_set[i] -=1
        return True