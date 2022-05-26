class Solution:
    def sortedSquares(self, nums):
        squares = []
        for i in nums:
            squares.append(i**2)
            squares.sort()
        return squares

def main():
    s= Solution()
    nums= list(map(int, input().split()))
    print(s.sortedSquares(nums))

if __name__ == '__main__':
    main()