# Problem 03: Print Numbers from 1 to N Using Recursion

## Problem Statement
Given a positive integer `N`, print numbers from `1` to `N` using recursion.

### Example
Input:
```text
5
```

Output:
```text
1
2
3
4
5
```

---

## Approach
To print numbers in ascending order, first make the recursive call and then print the current number while returning from the recursion stack.

### Base Case
```text
If n == 0, stop recursion.
```

---

## Dry Run

### Input
```text
N = 5
```

### Execution
```text
print_1_to_n(5)
│
├── print_1_to_n(4)
│   ├── print_1_to_n(3)
│   │   ├── print_1_to_n(2)
│   │   │   ├── print_1_to_n(1)
│   │   │   │   ├── print_1_to_n(0)
│   │   │   │   │   └── return
│   │   │   │   └── print(1)
│   │   │   └── print(2)
│   │   └── print(3)
│   └── print(4)
└── print(5)
```

### Output Flow
```text
1
2
3
4
5
```

---

## Python Code

python
n = int(input("Enter a number: "))

def print_1_to_n(n):
    if n == 0:
        return

    print_1_to_n(n - 1)
    print(n)

print_1_to_n(n)


---

## Sample Input
```text
Enter a number: 5
```

## Sample Output
```text
1
2
3
4
5
```

---

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
- Backtracking
- Base Case
- Call Stack

## Tags
```text
Recursion, DSA, Python
```
