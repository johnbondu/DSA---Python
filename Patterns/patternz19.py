# Pattern 19: Symmetric Void Pattern
#
# Example (n = 5):
#
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********

n = int(input("Enter No Of Rows: "))

# Initial spaces between left and right stars
space = 0

# Upper half of the pattern
for i in range(n):

    # Left stars
    print("*" * (n - i), end="")

    # Middle spaces
    print(" " * space, end="")

    # Right stars
    print("*" * (n - i), end="")

    # Increase spaces for next row
    space += 2

    print()

# Initial spaces for lower half
space = 2 * n - 2

# Lower half of the pattern
for j in range(1, n + 1):

    # Left stars
    print("*" * j, end="")

    # Middle spaces
    print(" " * space, end="")

    # Right stars
    print("*" * j, end="")

    # Decrease spaces for next row
    space -= 2

    print()

# Time Complexity: O(n²)
# Space Complexity: O(1)
