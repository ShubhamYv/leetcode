class Solution:
    def maxProfit(self, prices):
        l,r=0,1 #left buying nd right selling
        maxProfit=0
        while r < len(prices):
            #checking profit
            if prices[l] < prices[r]:
                profit= prices[r]- prices[l]
                maxProfit= max(profit, maxProfit)
            else:
            #if not profit
                l=r
            r+=1
        return maxProfit

def main():
    s= Solution()
    prices= list(map(int, input().split()))
    print(s.maxProfit(prices))

if __name__ == '__main__':
    main()