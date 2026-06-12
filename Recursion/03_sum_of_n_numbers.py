# Problem 04: Sum of First N Natural Numbers Using Recursion

## Problem Statement
Given a positive integer `N`, find the sum of the first `N` natural numbers using recursion.

### Example
Input:
```text
5
```

Output:
```text
15
```

---

## Approach
Each recursive call adds the current number `n` to the sum of numbers from `1` to `n-1`.

### Recursive Formula
```text
sum(n) = n + sum(n-1)
```

### Base Case
```text
sum(0) = 0
```

---

## Dry Run

### Input
```text
N = 5
```

### Execution
```text
sum(5)
= 5 + sum(4)
= 5 + 4 + sum(3)
= 5 + 4 + 3 + sum(2)
= 5 + 4 + 3 + 2 + sum(1)
= 5 + 4 + 3 + 2 + 1 + sum(0)
= 5 + 4 + 3 + 2 + 1 + 0
= 15
```



## Python Code

```python
n = int(input("Enter a number: "))

def sum_of_n_numbers(n):
    if n == 0:
        return 0

    return n + sum_of_n_numbers(n - 1)

print(sum_of_n_numbers(n))
```



## Complexity Analysis

### Time Complexity
```text
O(N)
```

### Space Complexity
```text
O(N)
```

(Recursive Call Stack)

---

## Concepts Used
- Recursion
- Base Case
- Recursive Relation
- Function Call Stack

## Tags
```text
Recursion, Mathematics, DSA, Python.
```
