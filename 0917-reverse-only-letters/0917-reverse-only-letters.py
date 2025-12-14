class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        i= 0
        j =len(s) - 1

        while i< j:
            if s[i].isalpha() and s[j].isalpha():
                temp=s[i]
                s[i]=s[j]
                s[j]= temp
                i +=1
                j -= 1
            elif not s[i].isalpha():
                i += 1
            else:
                j -=1
            
        return "".join(s)