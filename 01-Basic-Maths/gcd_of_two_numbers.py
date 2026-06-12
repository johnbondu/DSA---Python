# GCD of Two Numbers
# Time Complexity: O(log(min(a, b)))
# Space Complexity: O(1)

class Solution:
    def gcd(self, a, b):

        while b:
            a, b = b, a % b

        return a              # This are Just for 2 numbers 

#Finding GCD  using Eculid's theory
# this is for array 
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minimum = min(nums)
        maximum = max(nums)
        while maximum :
            minimum , maximum = maximum , minimum % maximum 
        return minimum
