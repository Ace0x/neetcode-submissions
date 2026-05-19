class PrefixTree:

    def __init__(self):
        self.dictionary = set()
        self.prefix_dict = {}

    def insert(self, word: str) -> None:
        s = ''
        for c in word:
            s += c
            self.prefix_dict[s] = word
        self.dictionary.add(word)

    def search(self, word: str) -> bool:
        if word in self.dictionary:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.prefix_dict:
            return True
        else:
            return False
        