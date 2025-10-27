from collections import defaultdict
from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_map = defaultdict(int)
        count = 0

        # Iterate through all pairs
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                if product in product_map:
                    count += product_map[product] * 8  # Each valid pair contributes 8 tuples
                product_map[product] += 1

        return count