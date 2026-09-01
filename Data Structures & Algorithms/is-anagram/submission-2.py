class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S, T = {}, {}
        for i in s:
            S[i] = S.get(i, 0) + 1
        for i in t:
            T[i] = T.get(i, 0) + 1
        return S == T