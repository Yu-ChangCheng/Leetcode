class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = defaultdict(list)
        for s in strs:
            token = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                token[i] += 1 
            result[tuple(token)].append(s)
        return list(result.values())

