class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        seen = set()
        q = deque([s])
        while q:
            s = q.popleft()
            for word in wordDict:
                if s.startswith(word):
                    new_s = s[len(word):]
                    if new_s == "":
                        return True
                    else:
                        if new_s not in seen:
                            q.append(new_s)
                            seen.add(new_s)
        return False
        