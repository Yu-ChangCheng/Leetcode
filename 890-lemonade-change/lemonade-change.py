class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        dollar_5 = 0
        dollar_10 = 0

        for n in bills:
            if n == 5:
                dollar_5 += 1
            elif n == 10:
                dollar_10 += 1
            
            change = n - 5
            if change == 5:
                if dollar_5:
                    dollar_5 -= 1
                else:
                    return False
            elif change == 15:
                if dollar_5 and dollar_10:
                    dollar_5 -= 1 
                    dollar_10 -= 1
                elif dollar_5 >=3:
                    dollar_5 -=3
                else:
                    return False
        return True