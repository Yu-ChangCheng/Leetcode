class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """

        sum_rolls = sum(rolls)
        m = len(rolls)
        remain = mean * (m + n) - sum_rolls
        if remain > n * 6 or remain < n:
            return []

        
        res = [1] * n
        remain -= n

        # i is used as index in the res
        i = 0
        while remain > 0:
            while remain > 5:
                res[i] += 5
                remain -= 5
                i += 1
            res[i] += remain
            return res
        return res
            
            
        
