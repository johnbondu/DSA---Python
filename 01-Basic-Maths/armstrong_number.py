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
n = int(input("Enter a Number: "))
s = Solution()
print(f"Is it Armstrong Number {n}.?")
print(s.isArmstrong(n))


Output --->

Enter a Number: 153
Is it Armstrong Number 153.?
True
