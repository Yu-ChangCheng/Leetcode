class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        commonPrefix = ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    return commonPrefix
            commonPrefix += char
        return commonPrefix

        # pre = strs[0]

        # for i in strs:
        #     while not i.startswith(pre):
        #         pre = pre[:-1]
        # return pre
            