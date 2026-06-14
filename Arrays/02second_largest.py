# Second Largest Element in an Array

Today I solved the Second Largest Element in an Array problem using an optimal approach.

## Problem

Given an array of integers, find the second largest element in the array. If there is no second largest element, return -1.

### Example

Input:
12 35 1 10 34 1

Output:
34

## My Approach

* Initialize two variables, `largest` and `second`, with very small values.
* Traverse the array only once.
* If the current element is greater than `largest`, update both `largest` and `second`.
* If the current element is smaller than `largest` but greater than `second`, update `second`.
* Return the second largest element.

## Python Code

```python
def second_largest(nums):
    largest = second = float('-inf')

    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second if second != float('-inf') else -1

print(second_largest(nums))
```

## Complexity

* Time Complexity: O(n)
* Space Complexity: O(1)

## What I Learned

* How to find the second largest element without sorting the array.
* How to maintain multiple variables during a single traversal.
* Why an O(n) solution is better than sorting-based approaches for this problem.

Part of my DSA preparation journey following Striver's A-Z DSA Sheet
-----> their is an another apporach which is by sorting

arr= sorted(set(num),reverse = True)
print(arr[1]
