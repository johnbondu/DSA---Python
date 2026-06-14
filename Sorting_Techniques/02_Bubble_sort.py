# Bubble Sort

Today I learned and implemented the Bubble Sort algorithm.

## Problem

Given an array of integers, sort the array in ascending order using Bubble Sort.

### Example

Input:
64 34 25 12 22 11 90

Output:
[11, 12, 22, 25, 34, 64, 90]

## My Approach

* Compare adjacent elements in the array.
* If the left element is greater than the right element, swap them.
* After each pass, the largest element moves to its correct position at the end of the array.
* Repeat the process until the entire array is sorted.

## Python Code

```python
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

arr = list(map(int, input().split()))
print(bubble_sort(arr))
```

## Complexity

* Time Complexity: O(n²)
* Space Complexity: O(1)

## What I Learned

* How Bubble Sort works by comparing adjacent elements.
* How larger elements gradually move to the end of the array after each pass.
* Swapping elements efficiently in Python.
* Why Bubble Sort is easy to understand but not suitable for large datasets.

Part of my DSA preparation journey following Striver's A-Z DSA Sheet.
