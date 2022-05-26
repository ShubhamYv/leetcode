class Solution:
    def findDup(self, nums):
        nums.sort()
        arr=[]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                arr.append(nums[i])
        return arr

def main():
    s= Solution()
    nums= list(map(int, input().strip().split()))
    print(s.findDup(nums))

if __name__ == '__main__':
    main()