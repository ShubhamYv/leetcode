class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefixscore= Counter()
        for word in words:
            for i in range(1, len(word)+1):
                prefixscore[word[:i]]+=1
        answer=[]
        for word in words:
            ans=0
            for i in range(1, len(word)+1):
                ans+= prefixscore[word[:i]]
            answer.append(ans)
        return answer
