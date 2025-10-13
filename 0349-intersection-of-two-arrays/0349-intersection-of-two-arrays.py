class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a={}
        for ele in nums1:
            if ele in a:
                a[ele] += 1
            else:
                a[ele] = 1
        result = []
        for ele in nums2:
            if ele in a:
                result.append(ele)
                a.pop(ele)
        return result