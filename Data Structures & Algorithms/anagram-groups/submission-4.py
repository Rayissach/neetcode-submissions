class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashS = defaultdict(list)
        for s in strs:
            countChar = [0] * 26
            for c in s:
                countChar[ord(c) - ord('a')] += 1
            hashS[tuple(countChar)].append(s)
        return list(hashS.values())