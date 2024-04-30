class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_s = s.split()
        list_s = list_s[::-1]
        s = " ".join(list_s)
        return s