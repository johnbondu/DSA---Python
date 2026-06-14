# Selection Sort

Today I learned and implemented the Selection Sort algorithm.

## Problem

Given an array of integers, sort the array in ascending order using Selection Sort.

### Example

Input:
64 25 12 22 11

Output:
[11, 12, 22, 25, 64]

## My Approach

* Traverse the array from left to right.
* For each position, find the smallest element in the remaining unsorted part of the array.
* Swap it with the current position.
* Repeat this process until the array becomes sorted.

## Python Code

```python
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

arr = list(map(int, input().split()))
print(selection_sort(arr))
```

## Complexity

* Time Complexity: O(n²)
* Space Complexity: O(1)

## What I Learned

* How Selection Sort works by repeatedly selecting the minimum element.
* How to keep track of the minimum element using its index.
* Swapping elements in Python.
* Difference between the sorted and unsorted portions of an array.

Part of my DSA preparation journey following Striver's A-Z DSA Sheet.
