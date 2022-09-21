class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1= len(s1)
        len2= len(s2)
        if len1> len2:
            return False
        #creating freq array
        countS1= [0]*26
        countS2= [0]*26
        for i in range(len1):
            countS1[ord(s1[i])- ord('a')]+=1
            countS2[ord(s2[i])- ord('a')]+=1
        #len2- len1 is the window slize
        for i in range(len2-len1):
            if countS1== countS2:
                return True
            #moving the window 
            countS2[ord(s2[i])- ord('a')]-= 1 #starting ele of window is removing
            countS2[ord(s2[i+len1])- ord('a')]+= 1 #new element is adding
        return countS1== countS2
