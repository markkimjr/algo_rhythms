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
# TODO find optimal solution
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


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)