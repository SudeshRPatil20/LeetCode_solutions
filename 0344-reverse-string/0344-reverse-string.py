class Solution:
    def reverseString(self, s: List[str]) -> None:
        l=0
        r=len(s)-1
        while r > l:
            temp = s[l]
            s[l]=s[r]
            s[r]= temp
            r -= 1
            l += 1

        return s 
        """
        Do not return anything, modify s in-place instead.
        
        """
        