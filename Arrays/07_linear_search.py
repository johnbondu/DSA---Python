Given an array of integers nums and an integer target, find the smallest index (0 based indexing) where the target appears in the array. If the target is not found in the array, return -1

link ---> :   https://takeuforward.org/plus/dsa/problems/linear-search?source=strivers-a2z-dsa-track
Example 1

Input: nums = [2, 3, 4, 5, 3], target = 3

Output: 1

Explanation:

The first occurence of 3 in nums is at index 1

Example 2

Input: nums = [2, -4, 4, 0, 10], target = 6

Output: -1

Explanation:

The value 6 does not occur in the array, hence output is -1

Now your turn!

Input: nums = [1, 3, 5, -4, 1], target = 1



Approach
Traverse the array from left to right.
Compare each element with the target.
If the target is found, return its index immediately.
If the traversal completes without finding the target, return -1.
Python Solution
class Solution:
    def linearSearch(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
--------->Alternative Solution Using enumerate()<--------
class Solution:
    def linearSearch(self, nums, target):
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1
-----> Dry Run
Input
nums = [2, 3, 4, 5, 3]
target = 3
Execution
Index	Value	Target Found?
0	2	No
1	3	Yes

Return:

1
Complexity Analysis
Time Complexity
O(n)

In the worst case, we may need to check every element.

Space Complexity
O(1)
