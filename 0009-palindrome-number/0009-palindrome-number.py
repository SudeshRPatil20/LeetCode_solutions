class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        original=x
        numreverse = 0
        while x > 0:
            last = x % 10
            numreverse=numreverse * 10 + last
            x = x // 10
        return numreverse == original