class Solution:
    def fib(self, n: int) -> int:
        # diry=[-1] * (n+1)
        # if n <= 1:
        #     return n
        # return self.fib(n-1) + self.fib(n-2)
    # this is not optimize because it gives complexity of 2^n
    # therefore the best approach is as follows (note do this infront of interviewer
        # def fib_helper(n):

        #     if (n <= 1):
        #         return n
            
        #     if diry[n] != -1:
        #         return diry[n]
            
        #     fib1=fib_helper(n-1)
        #     fib2 = fib_helper(n-2)

        #     diry[n-1] = fib1
        #     diry[n-2] = fib2

        #     ans = fib1 + fib2
        #     diry[n] = ans
        #     return diry[n]
        # return fib_helper(n)

    # if more optimize than use botom up approach memorization
        if n <= 1:
            return n
        
        dp = [0] * (n+1)
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
