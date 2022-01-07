class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self,word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node is None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfString = True
        print('Succesfully Inserted')

    def searchString(self,word):
        current = self.root
        for i in word:
            node = current.children.get(i)
            if node == None:
                return False
            current = node

        if current.endOfString == True:
            return True
        else:
            return False

def deleteString(root, word, index):
    ch = word[index]
    current = root.children.get(ch)
    canThisNodeBeDeleted = False

    if len(current.children) > 1:
        deleteString(current, word, index+1)
        return False

    if index == len(word) - 1:
        if len(current.children) >= 1:
            current.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True

    if current.endOfString == True:
        deleteString(current, word, index+1)
        return False

    canThisNodeBeDeleted = deleteString(current, word, index+1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False


newTrie = Trie()
newTrie.insertString('App')
newTrie.insertString('Appl')
deleteString(newTrie.root, "App", 0)
print(newTrie.searchString('App'))