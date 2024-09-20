class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        curr =[]
        def backtracking(i, curr, currSum):
            # print("i", i, "curr", curr, "currSum", currSum)
            if i + 1 > len(candidates) or currSum > target:
                return
            if currSum == target:
                self.res.append(curr[:])
                return
            curr.append(candidates[i])
            backtracking(i, curr, currSum + candidates[i])
            curr.pop()
            backtracking(i + 1, curr, currSum)
            
        backtracking(0, curr, 0)
        return self.res



        # self.res = []
        # curr = []
        
        # def backtracking(i, curr, currSum):
        #     if i > len(candidates) - 1 or currSum > target: # can't find the desired path
        #         return
        #     if currSum == target: # if find target append to the res
        #         self.res.append(curr[:])
        #         return
        #     curr.append(candidates[i]) # include the current candidates
        #     backtracking(i, curr, currSum + candidates[i]) # First backtracing
        #     curr.pop() # Exclud the current candidates
        #     backtracking(i+1, curr, currSum) # Second backtracing
        # backtracking(0, curr, 0)
        # return self.res

        # TC: O(number of candidates^max depth) -> O(n^(t/min(candidates))), where max depth = h ~= target val / smallest val 
        # b/c max depth of the tree is when it keeps adding the smallest element to the combination until it hits or exceeds target. 
        # SC: O(target val / smallest val in candidates) -> O(h), where max depth = h ~= target val / smallest val 