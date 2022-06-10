# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         start = maxLength = 0
#         usedChar = {}
#         for i in range(len(s)):
#             if s[i] in usedChar and start <= usedChar[s[i]]:
#                 start = usedChar[s[i]] + 1
#             else:
#                 maxLength = max(maxLength, i - start + 1)
#             usedChar[s[i]] = i
#         return maxLength

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        count = Counter()
        l = 0
        for r, c in enumerate(s):
            count[c] += 1
            while count[c] > 1:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans

def main():
    s= Solution()
    str= input()
    print(s.lengthOfLongestSubstring(str))

if __name__ == '__main__':
    main()
