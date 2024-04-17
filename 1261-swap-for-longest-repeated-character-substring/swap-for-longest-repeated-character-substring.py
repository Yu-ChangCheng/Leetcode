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

        # Count total occurrences of each character
        overall_count = Counter(text)
        max_len = 0

        # Evaluate each block to maximize the repeated substring
        for i in range(len(blocks)):
            char, length = blocks[i]
            # Try to extend this block by 1, limited by the total count of the character
            max_len = max(max_len, min(length + 1, overall_count[char]))

            # Check for possible merging with adjacent blocks of the same character separated by one different character
            if i < len(blocks) - 2 and blocks[i+1][1] == 1 and blocks[i+2][0] == char:
                # Calculate potential new length by merging current and next same-char block
                new_length = length + blocks[i+2][1]
                if overall_count[char] > new_length:
                    new_length += 1  # Check if there's at least one more 'char' to swap in
                max_len = max(max_len, new_length)

        return max_len