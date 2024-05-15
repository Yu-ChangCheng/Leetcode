class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        debt = defaultdict(int)
        for f, t, amount in transactions:
            debt[f] -= amount
            debt[t] += amount
        
        debt_list = [amount for amount in debt.values() if amount]
        n = len(debt_list)

        def backtracking(idx):
            while idx < n and debt_list[idx] == 0:
                idx += 1

            if idx == n:
                return 0
            
            ans = float('inf')

            for i in range(idx + 1, n):
                if debt_list[idx] * debt_list[i] < 0:
                    debt_list[i] += debt_list[idx]
                    ans = min(ans, backtracking(idx+1) + 1)
                    debt_list[i] -= debt_list[idx]
            return ans

        return backtracking(0)
                    
