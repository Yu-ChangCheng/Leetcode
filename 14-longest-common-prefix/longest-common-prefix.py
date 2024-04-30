class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre = strs[0]

        for i in strs:
            while not i.startswith(pre):
                pre = pre[:-1]
        return pre
            