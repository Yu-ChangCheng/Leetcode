class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t or len(s) < len(t):
            return ""
        dict_t = Counter(t)
        mini_len = float('Inf')
        mini_string = ""
        matched = 0
        start = 0

        for end in range(len(s)):
            if s[end] in dict_t:
                dict_t[s[end]] -= 1
                if dict_t[s[end]] == 0:
                    matched += 1

            while matched == len(dict_t) and start <= end:
                curr_len = end - start + 1
                if curr_len < mini_len:
                    mini_len = curr_len
                    mini_string = s[start: end + 1]

                if s[start] in dict_t:
                    if dict_t[s[start]] == 0:
                        matched -= 1
                    dict_t[s[start]] += 1
                start += 1
        return mini_string

