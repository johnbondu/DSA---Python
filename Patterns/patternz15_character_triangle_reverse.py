# pattren 15
# Concepts:
# - Nested Loops
# - ASCII Values
# - Character Conversion using chr()

Enter No of rows: 5
A B C D E 
A B C D 
A B C 
A B 
A 



n = int(input("Enter No of rows: "))

for i in range(n,0,-1):
    num = 65
    for j in range(1,i+1):
        print(chr(num),end = " ")
        num+=1
    print()
    
