def memorize(func):
    dictionary = {}
    def sub_function(*args):
        if args in dictionary:
            return dictionary[args]
        result = func(*args)
        dictionary[args] = result
        return result
    return sub_function



class Solution:
    def climbStairs(self, n: int) -> int:
        
        @memorize
        def dp(i):
            if i <= 2:
                return i
            return dp(i - 1) + dp(i - 2)
        return dp(n)
