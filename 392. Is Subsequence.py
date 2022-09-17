class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left, right, count=0, 0, 0
        while left< len(s) and right< len(t):
            if s[left]== t[right]:
                left+=1
                count+=1
            right+=1
        return count== len(s)
