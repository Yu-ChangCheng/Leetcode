class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t or len(s) < len(t):
            return ''

        countT, window = defaultdict(int), defaultdict(int)
        
        for c in t:
            countT[c] += 1 

        have = 0
        need = len(countT)
        res, resLen = [-1, -1], float('infinity') 

        l = 0 
        for r in range(len(s)):
            window[s[r]] += 1

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            while need == have:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1]    
            
                
                