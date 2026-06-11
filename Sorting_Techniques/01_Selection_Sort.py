
# Problem: Selection Sort in Python

## Problem Statement

Given an array of integers, sort the array in ascending order using the **Selection Sort** algorithm.

Selection Sort repeatedly finds the minimum element from the unsorted portion of the array and places it at the beginning.

---

## Example

### Input
```text
64 25 12 22 11
```

### Output
```text
[11, 12, 22, 25, 64]
```

---

## Approach

1. Assume the current element is the minimum.
2. Traverse the remaining unsorted array.
3. Find the actual minimum element.
4. Swap it with the current element.
5. Repeat until the array is sorted.

---

## Dry Run

### Input
```text
[64, 25, 12, 22, 11]
```

### Pass 1

```text
Minimum = 11

[11, 25, 12, 22, 64]
```

### Pass 2

```text
Minimum = 12

[11, 12, 25, 22, 64]
```

### Pass 3

```text
Minimum = 22

[11, 12, 22, 25, 64]
```

### Pass 4

```text
Minimum = 25

[11, 12, 22, 25, 64]
```

### Final Output

```text
[11, 12, 22, 25, 64]
```

---

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

---

## Sample Input

```text
64 25 12 22 11
```

## Sample Output

```text
[11, 12, 22, 25, 64]
```

---

## Complexity Analysis

### Time Complexity

```text
Best Case:    O(N²)
Average Case: O(N²)
Worst Case:   O(N²)
```

### Space Complexity

```text
O(1)
```

(In-place sorting algorithm)

---

## Key Points

- Simple sorting algorithm.
- In-place sorting.
- Not stable by default.
- Performs fewer swaps compared to Bubble Sort.

---

## Concepts Used

- Arrays
- Nested Loops
- Swapping
- Sorting Algorithms

---

## Tags

```text
Sorting, Selection Sort, Arrays, Python, DSA
```
