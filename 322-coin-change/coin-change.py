class Solution(object):
    def __init__(self):
        self.res = float('Inf')

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        q = deque([[amount, 0]])
        visited = set()

        while q:
            new_cur, n_coins = q.popleft()

            if new_cur == 0:
                return n_coins
         
            for c in coins:
                reminder = new_cur - c
                if reminder not in visited and reminder >= 0:
                    q.append([reminder, 1 + n_coins])
                    visited.add(reminder) 

        return -1

