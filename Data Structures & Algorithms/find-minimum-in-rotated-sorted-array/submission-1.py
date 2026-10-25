class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (r + l) // 2
            if nums[r] > nums[mid] > nums[l]:
                return nums[l]
            elif nums[mid] > nums[r]:
                if nums[l] > nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return nums[l]