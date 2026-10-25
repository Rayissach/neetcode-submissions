class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[r] < nums[l]:
                if nums[mid] > nums[r] >= target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1