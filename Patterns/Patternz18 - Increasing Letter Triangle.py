# Pattern 18: Increasing Letter Triangle
#
# Example (n = 5):
# E
# D E
# C D E
# B C D E
# A B C D E

n = int(input("Enter No of rows:"))

num = 64 + n

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(chr(num), end=" ")
        num += 1

    num = num - (i + 1)
    print()
