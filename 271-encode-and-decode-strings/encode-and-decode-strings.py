class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        strings = ""
        for s in strs:
            strings += str(len(s)) + "#" + s
        return strings 

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        # 25#gfghfg
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                    j += 1
            length = int(s[i:j]) #0:2 25
            res.append(s[j+1:j+1+length]) #3:28
            i = j+1+length # i=28
        return res
                
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))