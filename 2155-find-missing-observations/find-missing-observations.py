class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """

        m = len(rolls)
        total_required_sum = mean * (m + n)  # Total sum required to meet the mean
        sum_rolls = sum(rolls)  # Sum of given rolls
        remain = total_required_sum - sum_rolls  # Sum needed from missing rolls
        
        # If the remaining sum to find is out of possible range for n rolls, return empty
        if remain > n * 6 or remain < n:
            return []

        # Start each element in the result list with 1 (minimum possible value for a roll)
        result = [1] * n
        remain -= n  # Adjust remain after setting each to 1 (since 1*n is already used)
        
        # Distribute the remaining sum to make up to the mean requirement
        i = 0
        while remain > 0:
            add = min(5, remain)  # We can add up to 5 to each element (since max roll is 6)
            result[i] += add
            remain -= add
            i += 1  # Move to the next roll

        return result
            
        
