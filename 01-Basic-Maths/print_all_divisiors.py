class Solution:
    def divisors(self, n):
        l = []

        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                l.append(i)

                if i != n // i:
                    l.append(n // i)

        return sorted(l) 



here For first append the the number wich divides the nnumber  
let me explain by the example 2 * 18 = 36 here we store the 2 in the first append and 18 in the second append

Enter a number: 36
[1, 2, 3, 4, 6, 9, 12, 18, 36]






