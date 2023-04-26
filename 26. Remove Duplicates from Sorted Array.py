#when looping a list try to use while loop
#it does required to return the same length of list

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0 #initialize index
        while i < len(nums)-1: #make sure index won't goes above limit and it will updates even when item get deleted
            if nums[i] == nums[i+1]:
                del nums[i] #delete the item in original list
            else:
                i +=1   # if not the same will increase the index
        return len(nums)