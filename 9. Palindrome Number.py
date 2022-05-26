class Solution:
    def isPalindrome(self, x):
        temp = x
        rev = 0
        while (x > 0):
            dig = x % 10
            rev = rev * 10 + dig
            x = x // 10
        if (temp == rev):
            return "true"
        return "false"
def main():
    s= Solution()
    x= int(input())
    print(s.isPalindrome(x))

if __name__ == '__main__':
    main()

