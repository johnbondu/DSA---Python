# Largest Element in an Array

Today I solved a basic array problem: finding the largest element in an array.

## Problem

Given an array of integers, find the largest element present in the array.

link --> : https://takeuforward.org/plus/dsa/problems/largest-element?source=strivers-a2z-dsa-track

### Example

Input:
10 5 25 8 15

Output:
25

## My Approach

- Start by assuming the first element is the largest.
- Traverse through the array one by one.
- If a larger element is found, update the largest value.
- After checking all elements, return the largest element.

## Python Code

```python
nums = list(map(int, input("Enter an array: ").split()))

def find_largest_num(nums):
    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num

    return largest

#this is one of the optimal and best way to find largest number............

print(find_largest_num(nums))


their is another way to solve this problem by using the ("Max")
return max(nums)
