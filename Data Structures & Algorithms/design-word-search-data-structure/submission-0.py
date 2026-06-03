class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:

        def dfs(node, dword):
            if len(dword) < 1: return node.end

            c = dword[0]
            if c == ".":  
                for k, v in node.children.items():
                    if dfs(node.children[k], dword[1:]): return True
                return False
            else:
                if c not in node.children: 
                    return False
                else: 
                    return dfs(node.children[c], dword[1:])

        return dfs(self.root, word)
    


        
