this is quite differ from others because here we need apply a small logic just try to understand 
let me explain that here the main moto of a pattern is if the  index of row is odd starts with 1 otherwise 0 
and continoues the flow with alteranative nums.....(0,1)

Enter no of rows: 5
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 

n = int(input("Enter no of rows: "))
for i in range(1,n+1):
    if i % 2 == 0:
        start = 0
    else:
        start = 1
    for j in range(i):
        print(start, end = " ")
        start = 1 - start
    print()
