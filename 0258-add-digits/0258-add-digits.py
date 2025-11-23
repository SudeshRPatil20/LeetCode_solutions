class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        
        cnum = 0
        while num > 0:
            cnum += num % 10
            num = num // 10

        return self.addDigits(cnum)