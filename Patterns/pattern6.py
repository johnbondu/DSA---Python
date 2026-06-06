# these pattern is very similar to last paattern 
# But here we print numbers uinstead of astric(*)
problem --> https://takeuforward.org/plus/dsa/problems/pattern-6?source=strivers-a2z-dsa-track

# output --->
Enter number of lines :5
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 


n = int(input ("Enter number of lines :"))
for i in range(n,0,-1):
            for j in range(1,i+1):
                print(j,end = " ")
            print()
