class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        s_dict = defaultdict(int)
        for c in s: 
            s_dict[c] += 1
        
        for c in t:
            if c not in s_dict or s_dict[c] <= 0:
                return False
            else:
                s_dict[c] -= 1
        return True
        
        if len(s) != len(t):
            return False
        
        s_dict = defaultdict(int)
        for c in s:
            s_dict[c] += 1
        
        for c in t:
            if c not in s_dict or s_dict[c] <=0:
                return False
            else:
                s_dict[c] -= 1
        return True