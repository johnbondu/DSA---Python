# this is the third pattern here we are going to print the j which is innerloop  
# problem --> https://takeuforward.org/plus/dsa/problems/pattern-3?source=strivers-a2z-dsa-track
# Enter number of lines :5
# 1 
# 1 2 
# 1 2 3  
# 1 2 3 4 
# 1 2 3 4 5 

n = int(input("Enter number of lines :"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
        
    print()
