class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        rob1 = 0
        rob2 = 0
        #[rob1,rob2,(temp = max(n+rob1, rob2)),...]
        #[n,rob1,]
        # res=[]
        for n in nums:
          temp = max(n + rob1, rob2)
          rob1 = rob2
          rob2 = temp
        #   res.append(temp)
        # print(res)
        return rob2
        