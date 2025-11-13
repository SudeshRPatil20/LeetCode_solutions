from collections import Counter
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_len = 0

        for key in freq:
            if key + 1 in freq:
                max_len = max(max_len, freq[key] + freq[key + 1])

        return max_len
