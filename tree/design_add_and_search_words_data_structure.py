"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Example

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
"""

# brute force
# TODO review
class WordDictionary:

    def __init__(self):
        self.word_bank = {}

    def addWord(self, word: str) -> None:
        word_len = len(word)
        if self.word_bank.get(word_len):
            self.word_bank[word_len].append(word)
        else:
            self.word_bank[word_len] = [word]

        return None

    def search(self, word: str) -> bool:
        word_len = len(word)
        if not self.word_bank.get(word_len):
            return False
        for saved_word in self.word_bank[word_len]:
            if word == saved_word:
                return True
            is_same = True
            for i in range(word_len):
                if word[i] == ".":
                    continue
                if word[i] != saved_word[i]:
                    is_same = False
                    break
            if is_same:
                return True

        return False


class TrieNode:
    def __init__(self):
        self.children = {}
        self.last_word = False


class WordDictionaryDFS:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for l in word:
            if l not in cur.children:
                cur.children[l] = TrieNode()
            cur = cur.children[l]
        cur.last_word = True

    def searchWord(self, word: str) -> bool:
        def dfs(idx, node):
            cur = node
            for i in range(idx, len(word)):
                l = word[i]
                if l == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if l not in cur.children:
                        return False
                    cur = cur.children[l]
            return cur.last_word
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


if __name__ == "__main__":
    obj = WordDictionaryDFS()
    obj.addWord("blm")
    obj.addWord("bad")
    obj.addWord("sad")
    obj.addWord("happy")
    exists = obj.searchWord("bad")
    exists2 = obj.searchWord("b..")