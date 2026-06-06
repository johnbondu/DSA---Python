# in this pattern we print same number  thourgh out the length of n  here outer loop works on  row nothing but n
#inner loops works on the element which was going to print here i 
# problem --> https://takeuforward.org/plus/dsa/problems/pattern-4?source=strivers-a2z-dsa-track

# 1 1 
# 2 2 2 
# 3 3 3 3 
# 4 4 4 4 4 
# 5 5 5 5 5 5 


n = int(input ("Enter number of lines :"))
for i in range(1,n+1):
    for j in range(i+1):
        print(i,end=" ")
    print( )
  
