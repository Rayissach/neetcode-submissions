class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            n = [0] * 26
            for c in s:
                n[ord(c) - ord('a')] += 1
            res[tuple(n)].append(s)
        return list(res.values())