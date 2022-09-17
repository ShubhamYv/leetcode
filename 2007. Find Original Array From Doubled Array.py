class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        ans=[]
        dq= deque()
        for i in sorted(changed):
            if dq and i== dq[0]:
                dq.popleft()
                
            else:
                dq.append(i*2)
                ans.append(i)
        if dq:
            return []
        else:
            return ans
