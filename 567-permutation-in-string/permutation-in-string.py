class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_len, s2_len = len(s1), len(s2)
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:s1_len])

        for i in range(s1_len, s2_len):
            if s1_counter == s2_counter:
                return True
            s2_counter[s2[i-s1_len]] -= 1
            if s2_counter[s2[i-s1_len]] == 0:
                del s2_counter[s2[i-s1_len]]
            s2_counter[s2[i]] += 1

        return s1_counter == s2_counter
