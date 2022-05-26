class Solution:
    def findNumbers(self, nums):
        res=0
        for i in nums:
            if len(str(i))%2==0:
                res+=1
        return res

def main():
    s= Solution()
    nums= list(map(int, input().split()))
    print(s.findNumbers(nums))

if __name__ == '__main__':
    main()