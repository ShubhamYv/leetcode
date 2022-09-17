class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n= len(nums)
        m= len(multipliers)
        dp= [[0]*m for _ in range(m+1)]
        for i in reversed(range(m)):
            for j in range(i, m):
                k= i+ m- j- 1
                dp[i][j]= max(nums[i]* multipliers[k]+ dp[i+1][j], nums[j-m+n]* multipliers[k]+ dp[i][j-1])
        return dp[0][-1]
    
