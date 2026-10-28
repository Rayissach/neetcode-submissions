class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        sDict = {')': '(', ']': '[', '}': '{'}

        for i in s:
            if i in sDict:
                if stack and stack[-1] == sDict[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return False if stack else True