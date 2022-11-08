#%%
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class TrieNode():
    def __init__(self):
        self.children = 26*[None]
        self.isEndOfWord = False
class Trie:
    def __init__(self):
        self.root = self.getNode()

    def insert(self, word: str) -> None:
        pCrawl = self.root
        length = len(word)

        for level in range(length):
            index = self._charToIndex(word[level])

            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

        # mark last node as leaf
        pCrawl.isEndOfWord = True

        return None

    def _charToIndex(self,char):
        return ord(char)-ord('a')
        

    def search(self, word: str) -> bool:
        pCrawl = self.root
        length = len(word)

        for level in range(length):
            index = self._charToIndex(word[level])
            if not pCrawl.children[index]:
                return False

            pCrawl = pCrawl.children[index]

        return pCrawl.isEndOfWord
        

    def startsWith(self, prefix: str) -> bool:
        pCrawl = self.root
        length = len(prefix)

        for level in range(length):
            index = self._charToIndex(prefix[level])
            if not pCrawl.children[index]:
                return False

            pCrawl = pCrawl.children[index]

        return True

    def getNode(self):
        return TrieNode()

        


# Your Trie object will be instantiated and called as such:
trie = Trie()
words = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# for word in words:
#     trie.insert(word)
trie.insert("apple")

trie.search("apple")
trie.startsWith("app")
trie.search("app")
trie.insert("foo")
trie.insert("bar")
trie.search("foo")
# param_2 = obj.search('apple')
# param_3 = obj.startsWith(prefix)
# @lc code=end

