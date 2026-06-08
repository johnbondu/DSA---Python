# Pattern 12 - Number Symmetry Pattern
#
Enter No of rows: 5
1                 1 
1 2             2 1 
1 2 3         3 2 1 
1 2 3 4     4 3 2 1 
1 2 3 4 5 5 4 3 2 1 
#
# Concepts:
# - Nested Loops
# - Space Management
# - Increasing and Decreasing Number Sequences



n = int(input("Enter No of rows: "))
space = 2*(n-1)
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(1,space+1):
        print(" ",end=" ")
    for m in range(i,0,-1):
        print(m,end=" ")
    print()
    space -=2
