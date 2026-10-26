class Solution:
    def search(self, nums: List[int], target: int) -> int:
    #create two pointers
        l, r = 0, len(nums)-1
        #iterate over list and find target in either left or right sorted portion
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
        #check left sorted portion 
            elif nums[l] < nums[mid]:
                if nums[l] < target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        #check right sorted portion
            else:
                if  nums[mid] <= target < nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        #if not found return -1
        return -1
