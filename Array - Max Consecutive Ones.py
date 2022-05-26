class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count=0
        result=0
        for i in range(0, len(nums)):
            if nums[i]==0:
                count=0
            else:
                count+= 1
                result = max(result, count)
        return result

def main():
    s= Solution()
    nums= list(map(int, input().split()))
    print(s.findMaxConsecutiveOnes(nums))

if __name__ == '__main__':
    main()