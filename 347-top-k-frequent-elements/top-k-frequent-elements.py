class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # freq = 
        #[[1][2][3][4][5][6]]
        #[[3][2][1][0][0][0]]

        freq = [[] for i in range(len(nums) + 1)]
        count = defaultdict(int)
        
        for n in nums:
            count[n] += 1
        for i, value in count.items():
            freq[value].append(i)

        res = []
        for n in range(len(freq)-1, 0, -1):
            for c in freq[n]:
                res.append(c)
                if len(res) == k:
                    return res



