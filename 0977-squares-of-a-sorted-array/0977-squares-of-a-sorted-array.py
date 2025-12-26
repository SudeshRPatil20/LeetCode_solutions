class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        c=[0] * len(nums)
        k = len(nums) - 1

        while i <= j:
            if nums[i]*nums[i] > nums[j]*nums[j]:
                c[k] = nums[i]*nums[i]
                i += 1
            else:
                c[k] = nums[j]*nums[j]
                j -= 1
            
            k -= 1
        return c