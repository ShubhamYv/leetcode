class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        low=0
        high= sum(nums)
        for i, ele in enumerate(nums):
            high-= ele
            if low== high:
                return i
            low+= ele
        return -1
