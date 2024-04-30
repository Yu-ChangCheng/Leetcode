class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s) - 1
        carry = 0
        count = 0
        while (l > 0):
            ## even number with carry = 0, result even
            if int(s[l]) + carry == 0:
                carry = 0
                count += 1
            ## odd number with carry = 1, result even
            elif int(s[l]) + carry == 2:
                carry = 1
                count += 1
            ## odd number with carry = 0, result odd
            ## even number with carry = 1 result odd
            else:
                carry = 1
                count += 2
            l -= 1
        
        if carry == 1:
            count += 1
        return count
            