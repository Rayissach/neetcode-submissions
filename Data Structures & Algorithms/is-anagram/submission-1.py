class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ana = {}
        anaT = {}
        for i in s:
            ana[i] = 1 + ana.get(i, 0)
        for i in t:
            anaT[i] = 1 + anaT.get(i,0)
        return anaT == ana