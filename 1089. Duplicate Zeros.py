class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.

        TC: O(n^2) (since insert 0 and loop through the loop)
        SC: O(1)
        """
        i = 0
        length = len(arr)
        while i < length:
            if arr[i] == 0:
                arr.insert(i+1,0) #insert 0 after 0
                arr.pop() #remove the last element in list
                i += 2
            else:
                i += 1

                
