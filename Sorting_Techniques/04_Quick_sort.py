# Problem: Quick Sort in Python

## Problem Statement

Given an array of integers, sort the array in ascending order using the **Quick Sort** algorithm.

Quick Sort is a divide-and-conquer algorithm that selects a pivot element and partitions the array into two subarrays:
- Elements less than or equal to the pivot.
- Elements greater than the pivot.

The same process is recursively applied to the subarrays.

---

## Example

### Input
```text  --->
10 7 8 9 1 5
```

### Output
```text
1 5 7 8 9 10
```

---

## Approach

1. Select the first element as the pivot.
2. Partition the array into:
   - Left subarray containing elements ≤ pivot.
   - Right subarray containing elements > pivot.
3. Recursively sort the left and right subarrays.
4. Combine:
   - Sorted Left + Pivot + Sorted Right

---

## Dry Run

### Input
```text
[10, 7, 8, 9, 1, 5]
```

### Step 1

```text
Pivot = 10

Left  = [7, 8, 9, 1, 5]
Right = []
```

### Step 2

```text
Quick Sort Left

Pivot = 7

Left  = [1, 5]
Right = [8, 9]
```

### Step 3

```text
Quick Sort [1, 5]

Pivot = 1

Left  = []
Right = [5]

Result = [1, 5]
```

### Step 4

```text
Quick Sort [8, 9]

Pivot = 8

Left  = []
Right = [9]

Result = [8, 9]
```

### Final Combination

```text
[1, 5] + [7] + [8, 9]
= [1, 5, 7, 8, 9]

[1, 5, 7, 8, 9] + [10]
= [1, 5, 7, 8, 9, 10]
```

### Final Output

```text
1 5 7 8 9 10
```

---

## Python Code

```python
# Quick Sort Algorithm

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = list(map(int, input().split()))

result = quick_sort(arr)

print(*result)
```

---

## Sample Input

```text
10 7 8 9 1 5
```

## Sample Output

```text
1 5 7 8 9 10
```

---

## Complexity Analysis

### Time Complexity

```text
Best Case:    O(N log N)
Average Case: O(N log N)
Worst Case:   O(N²)
```

### Space Complexity

```text
O(N)
```

(Extra space used for left and right subarrays)

---

## Key Points

- Divide and Conquer algorithm.
- Faster than Bubble, Selection, and Insertion Sort for large datasets.
- Not a stable sorting algorithm.
- Widely used in real-world applications.
- Performance depends on pivot selection.

---

## Concepts Used

- Recursion
- Divide and Conquer
- Arrays
- Partitioning
- Sorting Algorithms

---

## Tags

```text
Sorting, Quick Sort, Recursion, Divide and Conquer, Arrays, Python, DSA
```
