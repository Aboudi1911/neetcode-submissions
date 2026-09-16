class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""
        k = ""
        for c in s:
            if c.isalnum():
                k += c
                r = c + r
        return (k.lower()==r.lower())

        