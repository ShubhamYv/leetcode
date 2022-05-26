class Solution:
    def maxProfit(self, prices):
        profit=0
        for i in range(1,len(prices)):
            if prices[i]> prices[i-1]:
                profit += (prices[i]-prices[i-1])
        return profit

def main():
    s= Solution()
    prices= list(map(int, input().split()))
    print(s.maxProfit(prices))

if __name__ == '__main__':
    main()