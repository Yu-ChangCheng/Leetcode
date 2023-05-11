class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = ""
        for s in strs:
            res += len(s) + "#" + s
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        res = []
        i = 0
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(s[i,j])
            res.append(res[j+1, j + length + 1])
            i = j + 1 + length
        return ress