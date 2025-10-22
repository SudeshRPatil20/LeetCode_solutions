class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a={}
        for num in nums:
            if num in a:
                a[num] +=1
            else:
                a[num] = 1
        return max(a, key=a.get)