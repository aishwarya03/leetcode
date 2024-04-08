class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = x
        if x >= 0:
            rev=0
            while x != 0:
                digit = x % 10
                rev = (rev * 10) + digit
                x = x // 10
            if a == rev:
                return True
            else:
                return False
        else:
            return False

num = Solution()
print(num.isPalindrome(121))