class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a, b = sorted((nums1, nums2), key=len)
        m, n = len(a), len(b)
        after = (m + n - 1) / 2
        # Determine i, j that a[0:i] + b[0:j] (exclusive) is the most small "after" numbers.
        # There could multiple pairs of such (i, j) if there are some duplicated numbers.
        # Each each such pair satisfies the following criteria at the same time:
        # 1) i + j == after
        # 2) (j>=1 and a[i] >= b[j-1]) or j==0
        # 3) (i>=1 and b[j] >= a[i-1]) or i==0
        lo, hi = 0, m
        while lo < hi:
            i = (lo + hi) / 2
            j = after - i
            cond1 = (j>=1 and a[i] >= b[j-1]) or j==0
            cond2 = (i>=1 and b[j] >= a[i-1]) or i==0
            if(cond1 and cond2):
                lo = i
                break
            elif(not cond1):
                assert(cond2)
                lo = i + 1
            else:
                assert(cond1)
                hi = i
        i = lo
        j = after - i
        nextfew = sorted(a[i:i+2] + b[j:j+2])
        return (nextfew[0] + nextfew[1 - (m+n)%2]) / 2.0