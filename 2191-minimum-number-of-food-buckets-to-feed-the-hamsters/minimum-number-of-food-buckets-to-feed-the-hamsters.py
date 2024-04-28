class Solution(object):
    def minimumBuckets(self, hamsters):
        """
        :type hamsters: str
        :rtype: int
        """
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