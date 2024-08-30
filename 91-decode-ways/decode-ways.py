class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # # edge case check
        # if not s or s[0] == '0':
        #     return 0
        
        # dp = [1] * len(s)
        
        # # Checking from the index 1 as first char can't be 0
        # for i in range(1,len(s)):
        #     # one digit check
        #     if int(s[i]) == 0: # if first char is 0, then there is no way we can start one digit at this position
        #         dp[i] = 0  
        #     else: 
        #         dp[i] = dp[i - 1] # if not 0 means that it can be as same as previous char

        #     # two digit check
        #     if 10 <= int(s[i-1:i+1]) <= 26: # [0:1], [1:2], [2:3], [3:4]
        #         if i >= 2: 
        #             dp[i] += dp[i-2] # current dp is the sum from previous two dp
        #         else: 
        #             dp[i] += dp[0] # when i = 1
        # return dp[-1]

        # Edge case check
        if not s or s[0] == '0':
            return 0

        # Initialize variables to represent dp[i-1] and dp[i-2]
        prev1 = 1  # This represents dp[i-1]
        prev2 = 1  # This represents dp[i-2]

        for i in range(1, len(s)):
            # Temporary variable to store the current dp value
            current = 0

            # Single character check
            if s[i] != '0':
                current = prev1

            # Two character check
            if 10 <= int(s[i-1:i+1]) <= 26:
                current += prev2

            # Update prev2 and prev1 for the next iteration
            prev2, prev1 = prev1, current

        return prev1