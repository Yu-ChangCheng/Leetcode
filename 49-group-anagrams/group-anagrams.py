class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # "abc", "bca"
        # [1,1,1,0,0,0,...,0] array of size 26 serve as the key of the string

        res = defaultdict(list)
        for s in strs:
            string_key = [0] * 26
            for c in s:
                string_key[ord(c) - ord('a')] += 1
            res[tuple(string_key)].append(s)
        return res.values()