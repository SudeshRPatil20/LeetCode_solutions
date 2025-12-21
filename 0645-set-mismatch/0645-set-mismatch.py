class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        duplicate = -1
        s = set()

        for num in nums:
            if num in s:
                duplicate = num
            s.add(num)

        missing = (n * (n + 1)) // 2 - (sum(nums) - duplicate)

        return [duplicate, missing]

            