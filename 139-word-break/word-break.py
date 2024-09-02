class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)  # Convert the wordDict list to a set for O(1) lookups
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True  # Base case: an empty string is always valid

        for i in range(len(s) - 1, -1, -1):  # Bottom-up DP
            for j in range(i + 1, len(s) + 1):  # Check every possible end index
                if s[i:j] in wordSet:  # O(1) lookup
                    dp[i] = dp[j]
                if dp[i]:  # Early exit if a valid segmentation is found
                    break

        return dp[0]

        # TC: O(n^2) + O(m) where n is the length of s, m is the words in wordDict
        # SC: O(n+m)