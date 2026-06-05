# LeetCode Problem Number - 9 Palindrome Number
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        rev =0 
        while x :
            d = x % 10
            rev =rev * 10 + d
            x = x // 10

        return temp == rev
