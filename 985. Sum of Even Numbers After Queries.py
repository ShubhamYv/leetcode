class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum=0
        for i in range(len(nums)):
            if nums[i]%2== 0:
                sum+= nums[i]
        list=[]
        for i in range(len(queries)):
            prev= nums[queries[i][1]]
            nums[queries[i][1]]+= queries[i][0]
            curr= nums[queries[i][1]]
            if prev% 2==0:
                if curr%2== 0:
                    sum+= curr- prev
                else:
                    sum-= prev
                    
            else:
                if curr%2== 0:
                    sum+= curr
            list.append(sum)
        return list
