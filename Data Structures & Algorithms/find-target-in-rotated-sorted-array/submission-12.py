class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]:
                #check if target is in sorted left half
                #if target is between left and mid
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                #check if targey is in sorted right half
                #is it between right and mid
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1