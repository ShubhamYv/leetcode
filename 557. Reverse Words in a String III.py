class Solution:
    def reverseWords(self, s: str) -> str:
        words= s.split()
        ans= " ".join(i[::-1] for i in words)
        return ans
