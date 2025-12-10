class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans1_list = []
        used = [False] * len(arr1)  

        arr2_pointer = 0
        while arr2_pointer < len(arr2):
            val = arr2[arr2_pointer]

            arr1_pointer = 0
            while arr1_pointer < len(arr1):
                if arr1[arr1_pointer] == val:
                    ans1_list.append(arr1[arr1_pointer])
                    used[arr1_pointer] = True
                arr1_pointer += 1

            arr2_pointer += 1
        ans2_list = []
        arr1_pointer = 0
        while arr1_pointer < len(arr1):
            if not used[arr1_pointer]:
                ans2_list.append(arr1[arr1_pointer])
            arr1_pointer += 1

        ans2_list.sort()

        return ans1_list + ans2_list
