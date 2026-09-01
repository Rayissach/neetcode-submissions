class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for i in s:
            if i.isalnum():
                res += i.lower()
        return True if res == res[::-1] else False
        