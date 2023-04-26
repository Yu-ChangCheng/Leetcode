class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        sum = []
        if len(num1) >= len(num2):
            num_long = num1
            num_short = num2
            num_short = num_short.zfill(len(num_long))
        else:
            num_long = num2
            num_short = num1
            num_short = num_short.zfill(len(num_long))

        for i in range(len(num_long))[::-1]:
            num_long_digit = ord(num_long[i]) - ord('0')
            num_short_digit = ord(num_short[i]) - ord('0')
            value = (num_long_digit + num_short_digit + carry) % 10
            carry = (num_long_digit + num_short_digit + carry) // 10
            sum.append(value)

        if carry:
            sum.append(carry)

        return "".join(str(x) for x in sum[::-1])
