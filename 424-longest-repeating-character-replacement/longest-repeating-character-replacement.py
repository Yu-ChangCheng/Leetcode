from collections import defaultdict

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
        max_freq = 0  # To track the maximum frequency of any character in the current window

        for r in range(len(s)):
            count[s[r]] += 1
            max_freq = max(max_freq, count[s[r]])  # Update max_freq with the new frequency of s[r]

            # If current window is not valid, shrink the window from the left
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            # Update the result with the maximum window length
            res = max(res, r - l + 1)

        return res
