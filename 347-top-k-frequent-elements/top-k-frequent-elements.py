class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        bucket = [[] for i in range(len(nums)+1)]
        for key, val in count.items():
            bucket[val].append(key)
        
        result = []
        c = 0
        for b in bucket[::-1]:
            for n in b:
                result.append(n)
                c += 1
                if k == c:
                    return result
            
            