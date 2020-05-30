"""
Trie is prefix tree, it's faster to search for partial string prefix like in phone directory.
"""


# Python program for insert and search 
# operation in a Trie 

# Example from : https://www.tutorialspoint.com/implement-trie-prefix-tree-in-python
  
class TrieNode: 
      
    # Trie node class 
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie: 
      
    # Trie data structure class 
    def __init__(self): 
        self.root = self.getNode() 
        self.charlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  
    def getNode(self): 
      
        # Returns new trie node (initialized to NULLs) 
        return TrieNode() 
  
    def _charToIndex(self,ch): 
          
        # private helper function 
        # Converts key current character into index 
        # use only 'a' through 'z' and lower case 
          
        return ord(ch)-ord('a') 
  
    def _inderxToChar(self, index):
        return self.charlist[index]

    def insert(self,key): 
          
        # If not present, inserts key into trie 
        # If the key is prefix of trie node,  
        # just marks leaf node 
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level]) 
  
            # if current character is not present 
            if not pCrawl.children[index]: 
                pCrawl.children[index] = self.getNode() 
            pCrawl = pCrawl.children[index] 
  
        # mark last node as leaf 
        pCrawl.isEndOfWord = True
  
    def search(self, key): 
          
        # Search key in the trie 
        # Returns true if key presents  
        # in trie, else false 
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level]) 
            if not pCrawl.children[index]: 
                return False
            pCrawl = pCrawl.children[index] 
  
        return pCrawl != None and pCrawl.isEndOfWord 

    def searchprefix(self, key):
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level]) 
            if not pCrawl.children[index]: 
                return []
            pCrawl = pCrawl.children[index] 
  
        # return all children.
        wordList =  self.returnAllChildren(pCrawl)
        for i in range(len(wordList)):
            wordList[i] = key +wordList[i]
    
        return wordList

    def returnAllChildren(self, node):
        print("returnAllChildren enter")
        if node.isEndOfWord:
            returnlist = [""]
        else:
            returnlist = []

        for index in range(len(node.children)):
            if node.children[index]:
                suffixList = self.returnAllChildren(node.children[index])

                if suffixList:
                    for i in range(len(suffixList)):
                                suffixList[i] =  self._inderxToChar(index) + suffixList[i]
                else:
                    suffixList.append(self._inderxToChar(index))

                returnlist = returnlist+suffixList

        print("returnAllChildren {}".format(returnlist))
        return returnlist

# driver function 
def main(): 
  
    # Input keys (use only 'a' through 'z' and lower case) 
    keys = ["the","a","there","therei","anaswe","any", 
            "by","their"] 
    output = ["Not present in trie", 
              "Present in trie"] 
  
    # Trie object 
    t = Trie() 
  
    # Construct trie 
    for key in keys: 
        t.insert(key) 
  
    # Search for different keys 
    #print("{} ---- {}".format("the",t.searchprefix("the"))) 
    print("{} ---- {}".format("t",t.searchprefix("t")))
    #rint("{} ---- {}".format("these",output[t.search("these")])) 
    #print("{} ---- {}".format("their",output[t.search("their")])) 
    #print("{} ---- {}".format("thaw",output[t.search("thaw")])) 


  
if __name__ == '__main__': 
    main() 