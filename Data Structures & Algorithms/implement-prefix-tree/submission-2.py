class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()



    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.eow = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            #print(c, cur.children)
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.eow 

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


"""class PrefixTree:

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
            return False"""
        