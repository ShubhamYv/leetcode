class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        fileDict= collections.defaultdict(list)
        res= list()
        for i in paths:
            directory, *files= i.split(' ')
            for j in files:
                fileName, content= j.split("(")
                fileDict['()'+content].append(directory+'/'+fileName)
        
        for i, j in fileDict.items():
            if len(j)> 1:
                res.append(j)
        return res
