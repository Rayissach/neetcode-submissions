class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        fin = {}
        for i in nums:
            fin[i] = 1 + fin.get(i, 0)
        for i, v in fin.items():
            if v > 1:
                return True
        return False