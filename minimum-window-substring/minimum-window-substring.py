class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        countT = Counter(t)
        have, need = 0 , len(countT)
        countS = defaultdict(int)
        res, res_len = [0, 0], float('Infinity')

        l = 0
        for r in range(len(s)):
            countS[s[r]] += 1
            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res_len = (r - l + 1)
                    res = [l, r]
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r+1] if res_len != float('Infinity') else ""


