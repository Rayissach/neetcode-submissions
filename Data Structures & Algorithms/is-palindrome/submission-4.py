class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for i in s:
            if i.isalnum():
                res += i
        l, r = 0, len(res)-1
        while l < r:
            while l < r and res[l].lower() != res[r].lower():
                return False
            l += 1
            r -= 1
        return True
        