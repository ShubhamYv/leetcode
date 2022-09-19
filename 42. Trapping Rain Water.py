class Solution:
    def trap(self, height: List[int]) -> int:
        n= len(height)
        l, r= n*[0], n*[0]
        l[0]= height[0]
        lMax= height[0]
        for i in range(n):
            if lMax< height[i]:
                lMax= height[i]
                l[i]= lMax
            else:
                l[i]= lMax
        rMax= height[n-1]
        for i in range(n-1, -1, -1):
            if rMax< height[i]:
                rMax= height[i]
                r[i]= rMax
            else:
                r[i]= rMax
                
        water=0
        for i in range(n):
            water= water+ min(l[i], r[i])- height[i]
        return water
