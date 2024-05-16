class Solution(object):
    def largestPalindromic(self, num):
        """
        :type num: str
        :rtype: str
        """
        counts = Counter(num)
        list_counts = sorted([[value, count] for value, count in counts.items()], key = lambda x: x[0])[::-1]
        left = ""
        mid = ""

        for value, count in list_counts:
            curr_c = value * (count // 2)
            if count % 2 == 0:
                left += curr_c
            else:
                left += curr_c
                mid = max(mid, value)
        left = left.lstrip('0')
        if left + mid + left[::-1]:
            return left + mid + left[::-1]
        else:
            return "0"
        
        counts = Counter(num) # {"9": 3}
        list_counts = sorted([[value, count] for value, count in counts.items()], key = lambda x: x[0])[::-1]
        left = ""
        mid = ""

        for value, count in list_counts:
            curr_c = value * (count // 2)
            if count % 2 == 0:
                left += curr_c
            else:
                left += curr_c
                mid = max(mid, value)
        left = left.lstrip('0')
        if left + mid + left[::-1]:
            return left + mid + left[::-1]
        else:
            return "0"
        
