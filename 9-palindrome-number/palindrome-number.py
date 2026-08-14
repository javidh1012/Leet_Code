class Solution:
    def isPalindrome(self, x: int) -> bool:
        # s = str(x)
        # if s == s[::-1]:
        #     return True
        # return False


        original_value = x
        reverse = 0

        if x < 0:
            return False

        while x > 0:
            reverse = reverse * 10 + x%10
            x//=10

        return original_value == reverse



