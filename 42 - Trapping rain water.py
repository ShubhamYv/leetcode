class Solution:
    def trap(self, height):
        n= len(height)
        left= n*[0]
        right= n*[0]
        left[0]= height[0]

        leftMax= height[0]
        for i in range(n):
            if leftMax< height[i]:
                leftMax= height[i]
                left[i]= leftMax
            else:
                left[i]= leftMax

        rightMax= height[n-1]
        for i in range(n-1, -1, -1):
            if rightMax< height[i]:
                rightMax= height[i]
                right[i]= rightMax
            else:
                right[i]= rightMax

        water=0
        for i in range(n):
            water= water+ min(left[i], right[i])- height[i]
        return  water

def main():
    s= Solution()
    n= int(input())
    arr= list(map(int, input().split()))
    print(s.trap(arr))

if __name__ == '__main__':
    main()