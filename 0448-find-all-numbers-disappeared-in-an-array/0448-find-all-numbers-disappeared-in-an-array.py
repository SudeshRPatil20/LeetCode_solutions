class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        c = list(range(1, n + 1))
        d = []
    
        num_set = set(nums)  

        for num in c:
            if num not in num_set:
                d.append(num)

        return d