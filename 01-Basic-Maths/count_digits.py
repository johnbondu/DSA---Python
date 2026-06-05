# Problem:
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

# LeetCode 1295 - Find Numbers with Even Number of Digits
# Difficulty: Easy
# Time Complexity: O(n * d)
# Space Complexity: O(1)
  class Solution:
    def findNumbers(self, nums: List[int]) -> int:
          n = len (nums)
          even = 0
          for i in range(n):
              count = 0
              while nums[i]:
                  d = nums[i] % 10 
                  count +=1
                  nums[i]= nums[i] // 10
              if count % 2 == 0:
                  even +=1
          return even
      # Alternative Apporoach
          # count = 0 
          # for num in nums:
          #     if len(str(num)) % 2 == 0:
          #         count +=1
          # return count        
