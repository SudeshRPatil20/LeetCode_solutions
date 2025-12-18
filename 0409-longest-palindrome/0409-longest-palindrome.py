class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1

        cot={}

        for char in s:
            if char in cot:
                cot[char] += 1
            else:
                cot[char] = 1
        count = 0
        old_ele = False
        for key in cot.values():
            if key % 2 == 0:
                count += key
            else:
                count += key -1
                old_ele = True
        if old_ele:
            count += 1
        
        return count
        
        if len(s) % 2 != 0:
            count += 2
        
        return count + 1