class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = deque()
        res = []

        for i, curr in enumerate(nums):
            while q and nums[q[-1]] < curr:
                q.pop()
            q.append(i)

            if q[0] == i-k:
                q.popleft()

            if i+1 >= k:
                res.append(nums[q[0]])
        return res