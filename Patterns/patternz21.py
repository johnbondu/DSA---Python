# Pattern 21: Hollow Rectangle Pattern
#
# Example (n = 5):
#
# * * * * *
# *       *
# *       *
# *       *
# * * * * *


# Approach 1: Direct Logic

n = int(input("Enter No Of Rows: "))

# Top Border
print("* " * n)

# Middle Rows
for i in range(1, n - 1):

    # Left Border
    print("*", end=" ")

    # Hollow Space
    print(" " * n, end=" ")

    # Right Border
    print("*", end=" ")

    print()

# Bottom Border
print("* " * n)

# Time Complexity: O(n²)
# Space Complexity: O(1)


# Approach 2: Row-Column Logic

n = int(input("Enter No Of Rows: "))

for i in range(n):
    for j in range(n):

        # Print star on boundaries
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

# Time Complexity: O(n²)
# Space Complexity: O(1)
