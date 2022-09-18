class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans=[]
        dict= {word[::-1]: i for i, word in enumerate(words)}
        for i, word in enumerate(words):
            if "" in dict and dict[""] != i and word== word[::-1]:
                ans.append([i, dict[""]])
            for j in range(1, len(word)+1):
                left= word[:j]
                right= word[j:]
                if left in dict and dict[left]!= i and right== right[::-1]:
                    ans.append([i, dict[left]])
                if right in dict and dict[right]!= i and left== left[::-1]:
                    ans.append([dict[right], i])
        return ans
                    
