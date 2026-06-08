# Pattern 14 - Character Triangle
#
# Example (n = 5):
# A
# A B
# A B C
# A B C D
# A B C D E
#
# Concepts:
# - Nested Loops
# - ASCII Values
# - Character Conversion using chr()

n = int(input("Enter No of rows: "))

for i in range(1,n+1):
    num = 65
    for j in range(1,i+1):
        print(chr(num),end = " ")    
        # print(chr(num + j) , end =" ")
        num+=1
    print()
    
