class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        maxLen = 0
        length = 0
        #iterate over original nums list
        for i in nums:
            #Check if the value has a left equivalent else initialize length to 0
            #if no left value that is -1 then it is the start of a sequence
            #e.g. 1 - 1 = 0 (is 0 in the list? if not it is start) initialize to 0
            if (i - 1) not in n:
                length = 0
                #Increment while i+length meaning right value is present in sequence
                #e.g. 1 + 1 = 2 (is 2 in sequence... yes) increment
                #e.g. 100 + 1 = 101 (is 101 in sequence... no) end while loop
                while (i + length) in n:
                    length += 1
            #return max
            maxLen = max(maxLen, length)
        return maxLen
