# Problem: Merge Sort in Python

## Problem Statement

Given an array of integers, sort the array in ascending order using the **Merge Sort** algorithm.

Merge Sort is a divide-and-conquer algorithm that recursively divides the array into two halves, sorts them independently, and then merges the sorted halves.

---

## Example

### Input
```text
38 27 43 3 9 82 10
```

### Output
```text
3 9 10 27 38 43 82
```

---

## Approach

1. Divide the array into two halves.
2. Recursively sort the left half.
3. Recursively sort the right half.
4. Merge the two sorted halves into a single sorted array.
5. Repeat until the entire array is sorted.

---

## Dry Run

### Input
```text
[38, 27, 43, 3, 9, 82, 10]
```

### Divide Phase

```text
[38, 27, 43, 3, 9, 82, 10]

          |
          ↓

Left  = [38, 27, 43]
Right = [3, 9, 82, 10]

          |
          ↓

[38] [27, 43]
[3, 9] [82, 10]

          |
          ↓

[38] [27] [43]
[3] [9] [82] [10]
```

### Merge Phase

```text
[27] + [43]
= [27, 43]

[38] + [27, 43]
= [27, 38, 43]

[3] + [9]
= [3, 9]

[82] + [10]
= [10, 82]

[3, 9] + [10, 82]
= [3, 9, 10, 82]

[27, 38, 43] + [3, 9, 10, 82]
= [3, 9, 10, 27, 38, 43, 82]
```

### Final Output

```text
3 9 10 27 38 43 82
```

---

## Python Code

```python
# Merge Sort Algorithm

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


arr = list(map(int, input().split()))

print(*merge_sort(arr))
```

---

## Sample Input

```text
38 27 43 3 9 82 10
```

## Sample Output

```text
3 9 10 27 38 43 82
```

---

## Complexity Analysis

### Time Complexity

```text
Best Case:    O(N log N)
Average Case: O(N log N)
Worst Case:   O(N log N)
```

### Space Complexity

```text
O(N)
```

(Extra space is used during merging)

---

## Key Points

- Divide and Conquer algorithm.
- Stable sorting algorithm.
- Guaranteed O(N log N) performance.
- Preferred when stable sorting is required.
- Commonly used in external sorting and large datasets.

---

## Concepts Used

- Recursion
- Divide and Conquer
- Arrays
- Merging
- Sorting Algorithms

