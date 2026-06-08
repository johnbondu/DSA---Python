Pattern 16 - Repeated Character Triangle

Output:
A
B B
C C C
D D D D
E E E E E

Concepts:
- Nested Loops
- Character Patterns
- ASCII Values
- Row-based Printing Logic


n = int(input("Enter No of rows: "))
num = 65
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(num),end = " ")
    num +=1   
    print()
    
