class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        hashmap = {} # 

        for i, a in enumerate(sorted(score, reverse = True)):
            hashmap[a] = i+1
        res = []
        for n in score:
            ans = str(hashmap[n])
            if hashmap[n] == 1:
                ans = "Gold Medal"
            elif hashmap[n] == 2:
                ans = "Silver Medal"
            elif hashmap[n] == 3:
                ans = "Bronze Medal"
            res.append(ans)
        return res