class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        a={}
        b={}

        if len(s) != len(t):
            return False
        
        for leter1, leter2 in zip(s, t):
            if (leter1 in a and a[leter1]!= leter2) or (leter2 in b and b[leter2]!=leter1):
                return False
            a[leter1] = leter2
            b[leter2] = leter1
        
        return True