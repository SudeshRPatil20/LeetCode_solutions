class Solution:
    def isHappy(self, n: int) -> bool:
        check={}


        while n not in check:
            check[n] = True

        
            count= 0
            temp= n
        
            while temp > 0:
                count += (temp % 10)**2
                temp = temp // 10 
        
            if count == 1:
                return True
            
            n=count

        return False