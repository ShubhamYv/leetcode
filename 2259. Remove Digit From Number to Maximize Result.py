class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        maxRes= 0
        for i in range(len(number)):
            if number[i]==digit:
                maxRes= max(maxRes, int(number[:i]+ number[i+1:]))
        return str(maxRes)
