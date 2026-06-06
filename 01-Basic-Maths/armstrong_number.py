# Armstrong Number
# Difficulty: Easy
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def isArmstrong(self, n):
        temp = n
        digits = len(str(n))
        total = 0
        while n:
            d = n % 10 
            total = total + d ** digits
            n = n// 10 
        return  temp == total 
