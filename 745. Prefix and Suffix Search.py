class WordFilter:

    def __init__(self, words: List[str]):
        self.pTrie = [None] * 27
        self.sTrie = [None] * 27
        for index in range(len(words)):
            self.insert(words[index], index, self.pTrie)
            self.insert(words[index][::-1], index, self.sTrie)

    def insert(self, word: str, index: int, trie: dict):
        for c in word:
            cval = ord(c) - 97
            if not trie[cval]: trie[cval] = [None] * 27
            trie = trie[cval]
            if not trie[26]: trie[26] = []
            trie[26].append(index)

    def retrieve(self, word: str, trie: dict) -> list:
        for c in word:
            cval = ord(c) - 97
            trie = trie[cval]
            if not trie: return []
        return trie[26]

    def f(self, pre: str, suf: str) -> int:
        pVals = self.retrieve(pre, self.pTrie)
        sVals = self.retrieve(suf[::-1], self.sTrie)
        svix, pvix = len(sVals) - 1, len(pVals) - 1
        while ~svix and ~pvix:
            sVal, pVal = sVals[svix], pVals[pvix]
            if sVal == pVal: return sVal
            if sVal > pVal: svix -= 1
            else: pvix -= 1
        return -1
