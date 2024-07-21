class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = defaultdict(int)
        l = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] += 1
            if (r-l+1) - max(count.values()) > k: # if current window is not valid
                count[s[l]] -= 1 # remove the left
                l += 1 # move left pointer
            else:
                # if current window is valid update the res with possible window length
                res = max(res, r-l+1) 
        return res

        
        