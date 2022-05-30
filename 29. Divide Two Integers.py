class Solution:
    def divide(self, dividend, divisor):
        if dividend * divisor > 0:
            res = abs(dividend) // abs(divisor)
        else:
            res = -(abs(dividend) // abs(divisor))
        intmin = -(2 ** 31)
        intmax = (2 ** 31) - 1
        if intmin <= res <= intmax:
            return res
        else:
            return intmax

def main():
    s= Solution()
    dividend= int(input())
    divisor= int(input())
    print(s.divide(dividend, divisor))

if __name__ == '__main__':
    main()