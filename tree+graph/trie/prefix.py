# Find shortest unique prefix to represent each word in the list.


class Node:
    def __init__(self, letter = '', isTerminal = False):
        self.letter = letter
        self.children = {}
        self.isTerminal = isTerminal
        self.freq = 0  # the number of visits during insert

class Trie:
    def __init__(self):
        self.root = Node('')

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                temp = Node(char)
                current.children[char] = Node(char)
            current.children[char].freq += 1
            current = current.children[char]
        current.isTerminal = True
        
    def contains(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.isTerminal

    def findPrefix(self, word):
        current = self.root
        prefix = ""
        for char in word:
            prefix += current.children[char].letter
            if current.children[char].freq == 1:
                return prefix
            else:
                current = current.children[char]
        return prefix



    
    
trie = Trie()

words = ["bearcat", "bert"]           
for w in words:
    trie.insert(w)
prefixes = []
for w in words:
    prefixes.append(trie.findPrefix(w))
print prefixes


