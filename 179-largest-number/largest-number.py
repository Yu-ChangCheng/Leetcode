class Solution(object):
    def largestNumber(self, nums):
        # Convert numbers to strings to prepare for comparison
        str_nums = list(map(str, nums))
        
        # Sort numbers based on a custom key without using cmp_to_key
        # Here, we sort by the value of concatenated pairs in reverse order
        str_nums.sort(key=lambda x: x*10, reverse=True)
        
        # Concatenate into a single string
        largest_num = ''.join(str_nums)
        
        # Convert to int and back to string to remove leading zeros
        return str(int(largest_num))