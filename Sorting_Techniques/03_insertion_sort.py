# Insertion Sort

Today I learned and implemented the Insertion Sort algorithm.

## Problem

Given an array of integers, sort the array in ascending order using Insertion Sort.

### Example

Input:
12 11 13 5 6

Output:
[5, 6, 11, 12, 13]

## My Approach

* Start from the second element of the array.
* Treat the first element as a sorted portion.
* Compare the current element with the elements before it.
* Shift larger elements one position to the right.
* Insert the current element into its correct position.
* Repeat the process until the entire array is sorted.

## Python Code

```python
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

arr = list(map(int, input().split()))
print(insertion_sort(arr))
```

## Complexity

* Time Complexity: O(n) in the best case, O(n²) in the average and worst cases.
* Space Complexity: O(1)

## What I Learned

* How Insertion Sort builds a sorted array one element at a time.
* The difference between swapping elements and shifting elements.
* Why Insertion Sort performs well when the array is already nearly sorted.
* How to insert an element into its correct position within a sorted portion of an array.

Part of my DSA preparation journey following Striver's A-Z DSA Sheet.
