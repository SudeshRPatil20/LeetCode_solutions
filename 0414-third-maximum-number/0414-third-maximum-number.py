class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        #without inbuild function

        # with inbuild function  
        if len(nums) <= 2:
            return max(nums)

        maximum= []
        for num in nums:
            if num not in maximum:
                maximum.append(num)
        
        numms=sorted(maximum)
        if len(numms) >= 3:
            return numms[-3]
        return max(numms)