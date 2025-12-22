class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # a={}
        # for num in nums:
        #     if num in a:
        #         a[num] +=1
        #     else:
        #         a[num] = 1
        # return max(a, key=a.get)

        # without hashmap
        vote_count=0
        candidate= 0

        for i in range(len(nums)):
            current_num=nums[i]
            if vote_count == 0:
                candidate= current_num
            if current_num == candidate:
                vote_count += 1
            else:
                vote_count -= 1
        return candidate