# Pattern 20: Symmetric Butterfly Pattern
#
# Example (n = 5):
#
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

n = int(input("Enter No of Rows: "))

# Initial spaces between left and right wings
space = 2 * n - 2

# Upper half of butterfly
for i in range(1, n + 1):

    # Left wing
    print("*" * i, end="")

    # Middle spaces
    print(" " * space, end="")

    # Right wing
    print("*" * i, end="")

    # Reduce spaces for next row
    space -= 2

    print()

# Initial spaces for lower half
space = 2

# Lower half of butterfly
for j in range(1, n + 1):

    # Left wing
    print("*" * (n - j), end="")

    # Middle spaces
    print(" " * space, end="")

    # Right wing
    print("*" * (n - j), end="")

    # Increase spaces for next row
    space += 2

    print()

# Time Complexity: O(n²)
# Space Complexity: O(1)
