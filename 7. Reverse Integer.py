### Two methods are not from ans
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_Negative = False # initialize if it is negative
        string_x=str(x) # convert int x into string 123 -> "123" , -123 -> "-123"
        string_x_reversed = string_x[::-1] # reverse the string is string[::-1]
        if string_x_reversed[-1] == "-": #check if it is negative
            string_x_reversed = string_x_reversed[:-1] #check if it is negative
            is_Negative = True

        if not is_Negative:
            int_x_reversed = int(string_x_reversed)
        else:
            int_x_reversed = -int(string_x_reversed)

        if int_x_reversed >= 2**31-1 or  int_x_reversed <= -2**31:
            return 0
        else:
            return int_x_reversed


# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#
#
#         if x >= 0:
#             is_Negative = False
#         else:
#             is_Negative = True
#
#         string_x=str(x)
#         string_x_reversed = string_x[::-1]
#         if is_Negative:
#             string_x_reversed = string_x_reversed[:-1] #remove the minus sign in string in the end ""-123" -> "321-" ->"321"
#         if not is_Negative:
#             int_x_reversed = int(string_x_reversed)
#         else:
#             int_x_reversed = -int(string_x_reversed)
#
#         if int_x_reversed >= 2**31-1 or  int_x_reversed <= -2**31:
#             return 0
#         else:
#             return int_x_reversed
