class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        balence_oprator={')':'(',']':'[','}':'{'}

        for char in s:
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if not stack or stack.pop() != balence_oprator[char]:
                    return False
        return len(stack) == 0