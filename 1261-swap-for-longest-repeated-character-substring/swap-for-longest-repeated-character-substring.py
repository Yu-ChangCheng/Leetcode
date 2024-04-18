class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        blocks = [] # [(a,3), (b,1), (a,3)]
        count = Counter(text) # {a:6, b:1}
        maxLength = 0
        
        i = 0
        while i < len(text):
            start = i
            while i < len(text) and text[start] == text[i]:
                i += 1
            blocks.append((text[start], i - start))

        # Evaluate each block to maximize the repeated substring
        for i in range(len(blocks)):
            maxLength = max(maxLength, min(blocks[i][1] + 1, count[blocks[i][0]]))

            if i + 2 < len(blocks) and blocks[i+1][1] == 1 and blocks[i+2][0] == blocks[i][0]:
                currLength = blocks[i][1] + blocks[i+2][1]
                if currLength < count[blocks[i][0]]:
                    currLength += 1
                maxLength = max(currLength, maxLength)
            
        return maxLength

        
        