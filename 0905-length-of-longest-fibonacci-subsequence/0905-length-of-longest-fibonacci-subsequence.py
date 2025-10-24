from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {x: i for i, x in enumerate(arr)}  # Map value to index
        dp = {}  # Dictionary to store the longest Fibonacci-like sequence ending at (i, j)
        max_len = 0
        
        for k in range(len(arr)):
            for j in range(k):
                x = arr[k] - arr[j]  # The expected previous element in the sequence
                i = index.get(x)  # Get index of x if it exists
                if i is not None and i < j:  # Ensure a valid Fibonacci sequence
                    dp[(j, k)] = dp.get((i, j), 2) + 1
                    max_len = max(max_len, dp[(j, k)])
                    
        return max_len if max_len >= 3 else 0