# Problem: Bubble Sort in Python

## Problem Statement

Given an array of integers, sort the array in ascending order using the **Bubble Sort** algorithm.

Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order. After each pass, the largest element moves to its correct position at the end of the array.

---

## Example

### Input
```text
64 34 25 12 22 11 90
```

### Output
```text
[11, 12, 22, 25, 34, 64, 90]
```

---

## Approach

1. Compare adjacent elements.
2. Swap them if they are in the wrong order.
3. After each pass, the largest unsorted element "bubbles up" to its correct position.
4. Repeat until the entire array is sorted.

---

## Dry Run

### Input
```text
[5, 1, 4, 2, 8]
```

### Pass 1

```text
[5, 1, 4, 2, 8]

Swap 5 and 1
[1, 5, 4, 2, 8]

Swap 5 and 4
[1, 4, 5, 2, 8]

Swap 5 and 2
[1, 4, 2, 5, 8]

No swap for 5 and 8

Result:
[1, 4, 2, 5, 8]
```

### Pass 2

```text
[1, 4, 2, 5, 8]

Swap 4 and 2
[1, 2, 4, 5, 8]
```

### Pass 3

```text
No swaps needed
Array is sorted
```

### Final Output

```text
[1, 2, 4, 5, 8]
```

---

## Python Code

```python
# Bubble Sort Algorithm

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

---

## Sample Input

```text
64 34 25 12 22 11 90
```

## Sample Output

```text
[11, 12, 22, 25, 34, 64, 90]
```

---

## Complexity Analysis

### Time Complexity

```text
Best Case:    O(N²)
Average Case: O(N²)
Worst Case:   O(N²)
```

### Optimized Bubble Sort

Using a swap flag:

```text
Best Case: O(N)
Average Case: O(N²)
Worst Case: O(N²)
```

### Space Complexity

```text
O(1)
```

(In-place sorting algorithm)

---

## Key Points

- Stable sorting algorithm.
- In-place sorting.
- Easy to understand and implement.
- Not efficient for large datasets.
- Largest element moves to the end after each pass.

---

## Concepts Used

- Arrays
- Nested Loops
- Swapping
- Sorting Algorithms

---

## Tags

```text
Sorting, Bubble Sort, Arrays, Python, DSA
```
