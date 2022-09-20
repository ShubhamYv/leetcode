class Solution:
    def longestPalindrome(self, s: str) -> int:
        dummySet= set()
        for i in s:
            if i not in dummySet:
                dummySet.add(i)
            else:
                dummySet.remove(i)
        if len(dummySet)!=0:
            return len(s)- len(dummySet)+1
        return len(s)
            
             
