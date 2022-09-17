class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high= 0, n
        while low < high:
            mid= (high+ low)//2
            if isBadVersion(mid):
                high= mid
            else:
                low= mid+1
        return low
