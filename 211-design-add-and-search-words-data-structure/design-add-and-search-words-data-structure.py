class WordDictionary(object):

    def __init__(self):
        self.word_dict = collections.defaultdict(set)
        
    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.word_dict[len(word)].add(word)

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if "." not in word:
            if word not in self.word_dict[len(word)]:
                return False
            else:
                return True
        
        for word_in_set in self.word_dict[len(word)]:
            matched = True
            for idx, search_char in enumerate(word):
                if word_in_set[idx] != search_char and search_char != ".":
                    matched = False
                    break
            if matched:
                return True
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)