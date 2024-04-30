class Solution(object):
    def minimumBuckets(self, hamsters):
        """
        :type hamsters: str
        :rtype: int
        """

        # If you find a house at index i, check i-1 doesn't have a bucket. If it does, continue
        # else: place a bucket at i+1 if you can or i-1 if you can't at i+1
        # if you can't find a bucket or place a bucket, then return -1
        # Time complexity: O(n), you only go through each element once
        # Space complexity: O(n), to build the array used for DP
        hamsters = list(hamsters)
        num = 0
        for i in range(len(hamsters)):
            if hamsters[i] == "H":
                if i > 0 and hamsters[i-1] == "B":
                    continue
                if i < len(hamsters) - 1 and hamsters[i+1] == ".":
                    hamsters[i+1] = "B"
                    num += 1
                    continue
                if i > 0 and hamsters[i-1] == ".":
                    hamsters[i-1] = "B"
                    num += 1
                    continue
                return -1
        return num