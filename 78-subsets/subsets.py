class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # self.res = []
        # curr = []
        # def backtracking(i, curr):
        #     if i == len(nums):
        #         self.res.append(curr[:])
        #         return
        #     curr.append(nums[i])
        #     backtracking(i+1, curr)
        #     curr.pop()
        #     backtracking(i+1, curr)
        # backtracking(0, curr)
        # return self.res

        # self.res = []
        # curr =[]

        # def backtracking(i, curr):
        #     if i == len(nums):
        #         self.res.append(curr[:])
        #         return
            
        #     curr.append(nums[i])
        #     backtracking(i+1, curr)
        #     curr.pop()
        #     backtracking(i+1, curr)
        
        # backtracking(0,curr)
        # print(self.res)
        # return self.res

        res = [[]]
        # nums.sort()
        for num in nums: 
            res += [ i + [num] for i in res]
        return res