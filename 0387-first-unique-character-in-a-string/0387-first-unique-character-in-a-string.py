class Solution:
    def firstUniqChar(self, s: str) -> int:
        # this is by hashmap
        dic={}

        for char in s:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
            
        for char in dic:
            if dic[char] == 1:
                return s.index(char)
        return -1
        
        
        
        
        
        
        
        
        
        
        
        # this is 2 pointer
        # i = 0
        
        # while i < len(s):
        #     j = 0
        #     is_unique=True

        #     while j < len(s):
        #         if i != j and s[i] == s[j]:
        #             is_unique = False
        #             break
        #         j +=1

        #     if is_unique:
        #         return i
            
        #     i += 1
            
        return -1