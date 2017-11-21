class Node:
    def __init__(self, letter = None, isTerminal = False):
        self.letter = letter
        self.children = {}
        self.isTerminal = isTerminal

class Trie:
    def __init__(self):
        self.root=Node()
        
    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = Node(letter)
            current = current.children[letter]
        current.isTerminal = True

    def contains(self, word):
        current=self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.isTerminal

    def containsPrefix(self, prefix):
        # return true if there is at least one word that starts with this prefix
        current=self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True
    
    def delete(self, current, word, index):

        # When the end of the word is reached, delete the node only if it's terminal
        if index == len(word):
            if not current.isTerminal:
                return False
            current.isTerminal = False
            return len(current.children) == 0
        node = current.children[word[index]]
        if self.delete(node, word, index + 1):
            current.children.pop(word[index])
            return len(current.children) == 0
        return False
                
    


trie = Trie()
trie.insert('abc')
trie.insert('axyz')
trie.insert('ax')
trie.insert('axyzd')
print trie.contains('axyz')
print trie.delete(trie.root, 'axyz', 0)

print trie.contains('axyz')
print trie.contains('axyzd')
print trie.contains('ax')
