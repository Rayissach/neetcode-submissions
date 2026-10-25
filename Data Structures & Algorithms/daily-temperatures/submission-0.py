class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        res = [0] * n
        stack = []
        for i in range(n):
            #check if stack isnt empty and a warmer temperature
            while stack and temps[i] > temps[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res