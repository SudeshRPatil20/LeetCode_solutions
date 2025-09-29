class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # Initialize the sequence with -1 (empty spots)
        result = [-1] * (2 * n - 1)
        
        # Function to place the integers in the sequence using backtracking
        def backtrack(index):
            # If we have placed all numbers, we are done
            if index == n + 1:
                return True
            
            # Try placing numbers from n down to 1
            for num in range(n, 0, -1):
                if num == 1:
                    # Special case for 1: It only appears once
                    if result.count(1) == 0:
                        result[result.index(-1)] = 1
                        if backtrack(index + 1):
                            return True
                        result[result.index(1)] = -1
                elif result.count(num) < 2:
                    # Ensure the number can occur twice
                    first_pos = result.index(-1)
                    second_pos = first_pos + num
                    if second_pos < len(result) and result[first_pos] == -1 and result[second_pos] == -1:
                        result[first_pos] = num
                        result[second_pos] = num
                        if backtrack(index + 1):
                            return True
                        result[first_pos] = -1
                        result[second_pos] = -1
            
            return False
        
        backtrack(1)  # Start at number 1
        return result
