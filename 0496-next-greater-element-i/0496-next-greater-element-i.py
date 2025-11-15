class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        next_gretor={}

        for num in nums2:
            while stack and num > stack[-1]:
                next_gretor[stack.pop()]=num
            stack.append(num)
        while stack:
            next_gretor[stack.pop()] = -1
        return [next_gretor[num] for num in nums1]

# most imp question asked in AWS, Google, Netflix, Meta, Paypal.