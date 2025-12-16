class Solution:
    def firstUniqChar(self, s: str) -> int:
        i = 0
        
        while i < len(s):
            j = 0
            is_unique=True

            while j < len(s):
                if i != j and s[i] == s[j]:
                    is_unique = False
                    break
                j +=1

            if is_unique:
                return i
            
            i += 1
            
        return -1