class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            j+=1
            i+=1
        if len(word1)>len(word2):
            result.append(word1[i:])
        else:
            result.append(word2[j:])        
        return ''.join(result)