class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        #[-4,-1,-1,0,1,2]
        for i in range(len(nums)-2):
            l, r = i + 1, len(nums)-1
            #Check for duplicates of i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                currSum =  nums[i] + nums[l] + nums[r]
                if currSum < 0:
                    l += 1
                elif currSum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    #Check for left and right duplicates
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
                    l += 1
        return res
                    
