class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_s = s.split(" ")
        list_s = list_s[::-1]
        new_list_s = []
        for i, word in enumerate(list_s):
            if "" != word:
                new_list_s.append(word)

        s = " ".join(new_list_s)
        s = s.lstrip(" ")
        s = s.rstrip(" ")
        return s

        # or 

        # list_s = s.split()
        # list_s = list_s[::-1]
        # return s