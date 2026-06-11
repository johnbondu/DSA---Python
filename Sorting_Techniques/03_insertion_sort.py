# Problem: Insertion Sort in Python

## Problem Statement

Given an array of integers, sort the array in ascending order using the **Insertion Sort** algorithm.

Insertion Sort builds the sorted array one element at a time by inserting each element into its correct position.

---

## Example

### Input
```text
12 11 13 5 6
```

### Output
```text
[5, 6, 11, 12, 13]
```

---

## Approach

1. Start from the second element.
2. Store the current element as `key`.
3. Compare it with elements on its left.
4. Shift larger elements one position to the right.
5. Insert the `key` at its correct position.
6. Repeat until the array is sorted.

---

## Dry Run

### Input
```text
[12, 11, 13, 5, 6]
```

### Pass 1

```text
Key = 11

[12, 11, 13, 5, 6]

Shift 12 right

[12, 12, 13, 5, 6]

Insert 11

[11, 12, 13, 5, 6]
```

### Pass 2

```text
Key = 13

Already in correct position

[11, 12, 13, 5, 6]
```

### Pass 3

```text
Key = 5

Shift 13, 12, 11 right

[11, 12, 13, 13, 6]
[11, 12, 12, 13, 6]
[11, 11, 12, 13, 6]

Insert 5

[5, 11, 12, 13, 6]
```

### Pass 4

```text
Key = 6

Shift 13, 12, 11 right

[5, 11, 12, 13, 13]
[5, 11, 12, 12, 13]
[5, 11, 11, 12, 13]

Insert 6

[5, 6, 11, 12, 13]
```

### Final Output

```text
[5, 6, 11, 12, 13]
```

---

## Python Code

```python
# Insertion Sort Algorithm

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

---

## Sample Input

```text
12 11 13 5 6
```

## Sample Output

```text
[5, 6, 11, 12, 13]
```

---

## Complexity Analysis

### Time Complexity

```text
Best Case:    O(N)
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

- Stable sorting algorithm.
- In-place sorting.
- Efficient for small datasets.
- Performs well on nearly sorted arrays.
- Commonly used as a building block in advanced sorting algorithms.

---

## Concepts Used

- Arrays
- Sorting Algorithms
- Shifting Elements
- Nested Loops

---

## Tags

```text
Sorting, Insertion Sort, Arrays, Python, DSA
```
