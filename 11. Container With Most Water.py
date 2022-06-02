class Solution:
    def maxArea(self, height):
        left,right =0, len(height)-1
        result = 0
        
        while left < right:
            water = (right-left) * min(height[left], height[right])
            if water > result:
                result = water
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return result
    
def main():
    height = int(input())
    ob= Solution()
    print(ob.maxArea(height))

if __name__ == '__main__':
    main()