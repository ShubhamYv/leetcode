class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2==0:
            return n*1
        else: 
            return n*2
