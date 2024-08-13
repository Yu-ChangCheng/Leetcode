class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        self.res = []
        curr = []
        
        def backtracking(i, curr, currSum):
            if i > len(candidates) - 1 or currSum > target:
                return
            if currSum == target:
                self.res.append(curr[:])
                return
            curr.append(candidates[i]) # include the current candidates
            backtracking(i, curr, currSum + candidates[i]) # First backtracing
            curr.pop() # Exclud the current candidates
            backtracking(i+1, curr, currSum) # Second backtracing
        backtracking(0, curr, 0)
        return self.res

        # TC: O(number of candidates^max depth), where max depth(h) ~= target val / smallest val 
        # b/c max depth of the tree is when it keeps adding the smallest element to the combination until it hits or exceeds target. 
        # SC: O(target val / smallest val in candidates) 