class Node:
    def __init__(self):
        self.d = {}
        self.eow = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.d:
                node.d[c] = Node()
            node = node.d[c]

        node.eow = True

    def travel(self, node, word, i):
        if i == len(word):
            return node.eow

        c = word[i]

        if c == ".":
            for child in node.d.values():
                if self.travel(child, word, i + 1):
                    return True
            return False

        if c not in node.d:
            return False

        return self.travel(node.d[c], word, i + 1)

    def search(self, word: str) -> bool:
        return self.travel(self.root, word, 0)
