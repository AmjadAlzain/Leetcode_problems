class Solution:
    def isPalindrome(self, x: int) -> bool:
      """ Returns if a number is a palindrome number or not
      >>> It inputs the int number x and the output is a bool true or false
      """
        reverse = 0
        r = 0
        n = x
        while(x > 0):
            r = x % 10
            reverse = r + 10 * reverse
            x //= 10
        print(reverse)
        if (n == reverse):
            return True
        else:
            return False
