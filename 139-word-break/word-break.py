class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # seen = set()
        # wordDictSet = set(wordDict)
        # q = deque([s])
        # while q:
        #     s = q.popleft()
        #     for word in wordDictSet:
        #         if s[:len(word)] in wordDictSet:
        #             new_s = s[len(word):]
        #             if new_s == "":
        #                 return True
        #             else:
        #                 if new_s not in seen:
        #                     q.append(new_s)
        #                     seen.add(new_s)
        # return False









        wordSet = set(wordDict)  # Convert the wordDict list to a set for O(1) lookups
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True  # Base case: an empty string is always valid

        for i in range(len(s) - 1, -1, -1):  # Bottom-up DP
            for j in range(i + 1, len(s) + 1):  # Check every possible end index
                if dp[j] and s[i:j] in wordSet:  # O(1) lookup
                    dp[i] = True
                    break   # Early exit if a valid segmentation is found
                    
        return dp[0]

        # TC: O(n^2) + O(m) where n is the length of s, m is the words in wordDict
        # SC: O(n+m)
        