class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Step 1: Check if the lengths of both strings are equal.
        # If they are not, they can't be anagrams.
        if len(s) != len(t):
            return False
        
        # Step 2: Create a dictionary to count the frequency of each character in string s.
        s_dict = defaultdict(int)
        
        # Step 3: Populate the dictionary with counts of each character in s.
        for c in s:
            s_dict[c] += 1
        
        # Step 4: Check each character in t against the dictionary.
        for c in t:
            # If a character in t is not in the dictionary or its count is zero, 
            # then s and t are not anagrams.
            if c not in s_dict or s_dict[c] <= 0:
                return False
            else:
                # Otherwise, decrement the count of the character.
                s_dict[c] -= 1
        
        # Step 5: If all characters match correctly, s and t are anagrams.
        return True
        # Space: O(k) where k is the number of unique characters
        # Time: O(2n) = O(n) where n length of s and t