// https://leetcode.com/problems/design-search-autocomplete-system

class Trie:
    def __init__(self):
        self.root={}

    def insert(self,sentence):
        cur=self.root
        for l in sentence:
            if l not in cur:
                cur[l]={}
            cur=cur[l]
        cur['#']=sentence
    
    def search(self,prefix,cur=None):
        if not cur:
            cur=self.root
        
        for c in prefix:
            if c not in cur:
                return []
            cur=cur[c]

        ans=[]

        for k in cur:
            if k=="#":
                ans.append(cur[k])

            ans=[]

        for k in cur:
            if k=="#":
                ans.append(cur[k])
            else:
                ans+=self.search('',cur[k])

        return ans


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.lookup={}

        for i,s in enumerate(sentences):
            self.lookup[s]=times[i]

        self.trie=Trie()

        for s in sentences:
            self.trie.insert(s)
        self.keyword=""

    def input(self, c: str) -> List[str]:
        if c=="#":
            self.lookup[self.keyword]=self.lookup.get(self.keyword,0)+1
            self.trie.insert(self.keyword)
            self.keyword=""
            return []
        else:
            self.keyword+=c
            lst=self.trie.search(self.keyword)
            lst.sort(key=lambda x:(-self.lookup[x],x))
            return lst[:3]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)