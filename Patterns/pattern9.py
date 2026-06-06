#The pattern is diamond shape using astric 
problem ----> https://takeuforward.org/plus/dsa/problems/pattern-9?source=strivers-a2z-dsa-track


Enter number of lines :5
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 


n = int(input ("Enter number of lines :"))
for i in range(1,n+1):
    #for space
    for j in range(n-i):
        print(" ",end=" ")
    #for astric
    for k in range(2*i-1):
        print("*",end =" ")
    #for new line
    print()

for i in range(n-1,0,-1):
    #for space 
    for j in range(n-i):
        print(" ",end=" ")
    #for pyramid
    for k in range(2*i-1):
        print("*",end=" ")
    print( )

