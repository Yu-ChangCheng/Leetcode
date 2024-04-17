class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        # Collecting blocks of consecutive characters
        blocks = []
        i = 0
        n = len(text)

        while i < n:
            start = i
            while i < n and text[i] == text[start]:
                i += 1
            length = i - start
            blocks.append((text[start], length))

        overall_count = Counter(text)
        max_len = 0

        # To maximize the repeated substring
        for i, (char, length) in enumerate(blocks):
            max_len = max(max_len, min(length + 1, overall_count[char]))  # Extend block by 1 if possible
            
            # Try to merge with next same char block if there's exactly one different char in between
            if i < len(blocks) - 2 and blocks[i+1][1] == 1 and blocks[i+2][0] == char:
                # Calculate potential new length by merging current and next same-char block
                new_length = length + blocks[i+2][1]
                if overall_count[char] > new_length:  # Check if there's at least one more 'char' to swap in
                    new_length += 1
                max_len = max(max_len, new_length)
            
            # Also consider just the longest possible sequence without swaps if blocks are not consecutive
            max_len = max(max_len, min(overall_count[char], length))

        return max_len