class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a={}

        for ele in nums:
            if ele in a:
                a[ele] += 1
            else:
                a[ele] = 1
            
        for ele in a:
            if a[ele] > 1:
                return ele