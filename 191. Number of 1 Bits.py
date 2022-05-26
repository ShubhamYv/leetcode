class Solution:
    def hammingWeight(self, n):
        n= int(n)
        res=0
        while n:
            n &= n-1
            res+=1
        return res