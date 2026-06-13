# Prime Number Check
# Difficulty: Easy
# Time Complexity: O(sqrt(n))
# Space Complexity: O(1)

n = int(input())

if n <= 1:
    print("Not a prime number")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

OUTPUT --->
37
Prime number

