class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = collections.Counter(s1)
        left,right = 0,0
        s1_len = len(s1)
        while(right < len(s2)):
            letter = s2[right]
            if letter not in count or count[letter] == 0:
                while(s2[left] != letter):
                    if s2[left] in count:
                        count[s2[left]]+=1
                        s1_len+=1
                    left+=1
                if s2[left] in count:
                    count[s2[left]]+=1
                    s1_len+=1
                left+=1
            if letter in count:
                count[letter]-=1
                s1_len -=1
                if s1_len == 0:
                    return True
            right+=1
        return False