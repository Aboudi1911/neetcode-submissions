class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = ""
        for c in s:
            if c.isalnum():
                k += c.lower()
        return (k==k[::-1])

        