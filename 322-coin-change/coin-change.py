class Solution(object):
    def __init__(self):
        self.res = float('Inf')

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        q = deque()
        q.append([amount,0])
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
        
        dp = [amount+1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-c])
        return dp[amount] if dp[amount] != amount + 1 else -1
