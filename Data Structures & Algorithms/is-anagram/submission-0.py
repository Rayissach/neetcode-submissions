class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = Counter(s)
        t2 = Counter(t)
        return s1 == t2