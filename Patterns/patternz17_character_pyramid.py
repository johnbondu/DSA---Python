# Pattern 17: Alpha Hill Pattern
# Example:
#         A
#       A B A
#     A B C B A
#   A B C D C B A
# A B C D E D C B A

n = int(input("Enter No of Rows: "))

for i in range(1, n + 1):
    num = 65

    # Spaces
    for s in range(n - i):
        print(" ", end=" ")

    # Increasing characters
    for j in range(1, i + 1):
        print(chr(num), end=" ")
        num += 1

    # Decreasing characters
    num -= 2
    for k in range(i - 1, 0, -1):
        print(chr(num), end=" ")
        num -= 1

    print()
