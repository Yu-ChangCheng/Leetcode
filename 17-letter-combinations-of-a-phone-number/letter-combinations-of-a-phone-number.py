class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_to_char = { 
            "2": "abc", 
            "3": "def", 
            "4": "ghi", 
            "5": "jkl", 
            "6": "mno", 
            "7": "pqrs", 
            "8":"tuv",  
            "9":"wxyz"}
        
        res=[]
        if len(digits) ==0:
            return res
        
        curr = ""
        def backtracking(i , curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            
            for c in digit_to_char[digits[i]]:
                backtracking(i+1, curr+c)
        backtracking(0, curr)
        return res