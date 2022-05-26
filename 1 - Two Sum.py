"""1. optimal approach"""

class Solution:
    def twoSum(self, nums, target):
        dict={}
        for i, n in enumerate(nums):
            if n in dict:
                return [dict[n], i]
            else:
                dict[target-n]= i





# """2. Optimal approach"""
#
#
# class Solution:
#     def twoSum(self, nums, target):
#         prevMap= {}
#         for i, n in enumerate(nums):
#             diff= target-n
#             if diff in prevMap:
#                 return [prevMap[diff], i]
#             prevMap[n]=i
#         return



# """3. brute force approach"""

# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 sum= nums[i]+nums[j]
#                 if sum== target:
#                     return [i,j]





def main():
    s= Solution()
    nums= list(map(int, input().split()))
    target= int(input())
    print(s.twoSum(nums, target))

if __name__ == '__main__':
    main()