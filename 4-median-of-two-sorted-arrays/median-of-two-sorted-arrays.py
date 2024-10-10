class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2 
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A): # A is shorter and B is longer
            A, B = B, A
        
        l, r = 0, len(A) - 1 # start BS in A

        while True:
            i = (l + r) // 2 # A (i is the mid index of A)
            j = half - i - 2 # B (j is the mid index of B)

            Aleft = A[i] if i >= 0 else -float('Inf')
            Aright = A[i + 1] if i + 1 < len(A) else float('Inf')
            Bleft = B[j] if j >= 0 else -float('Inf')
            Bright = B[j+1]if j + 1 < len(B) else float('Inf')

            # if partition is valid
            if Aleft <= Bright and Bleft <= Aright:
                # odd 
                if total % 2:
                    return min(Aright, Bright)
                # even
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            
            # if partition is not valid
            elif Aleft > Bright:
                r = i - 1
            else: 
                l = i + 1
