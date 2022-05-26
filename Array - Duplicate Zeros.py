class Solution:
    def duplicateZeros(self, arr):
        res = [] * arr
        index = 0
        for i in range(len(res)):
            if arr[index] != 0:
                res[i] = arr[index]
            else:
                res[i] = 0
                if i + 1 < len(res):
                    res[i + 1] = 0
                    i += 1
                index += 1
        for i in range(len(res)):
            arr[i] = res[i]

def main():
    s= Solution()
    nums= list(map(int, input().split()))
    print(s.duplicateZeros(nums))

if __name__ == '__main__':
    main()


"""OUTPUT IS NOT COMING"""

"""Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
"""