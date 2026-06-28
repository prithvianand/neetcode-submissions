class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToclosedMapping = { ')':'(','}':'{', ']':'['}
        for char in s:
            if char in openToclosedMapping:
                if stack and stack[-1] == openToclosedMapping[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
        