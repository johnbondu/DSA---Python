 returning factorial  of a number ---->


required out put like -->

  Enter a number : 5
120
#calling itself until base condition

factorial(5)
= 5 * factorial(4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1
= 120



def factorial(n):
    if n==0 or n == 1:
        return 1
    return n * factorial(n-1) 
n = int(input(f"Enter a number : "))

print(factorial(n))
