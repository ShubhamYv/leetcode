class Solution:
    def runningSum(self, nums):
        ans=[]
        tmp=0
        for i in nums:
            tmp+=i
            ans.append(tmp)
        return ans

def main():
    s= Solution()
    nums= list(map(int, input().split()))
    print(s.runningSum(nums))

if __name__ == '__main__':
    main()