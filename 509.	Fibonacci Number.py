class Solution:
    def fib(self, n: int) -> int:
        dp= [-1 for _ in range(n+1)]
        if n==0 or n==1:
            return n
        if dp[n]!=-1:
            return dp[n]
        x= self.fib(n-1)
        y= self.fib(n-2)
        dp[n]= x+y
        return dp[n]
