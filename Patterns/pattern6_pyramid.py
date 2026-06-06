hiii welcome this is quite diff from other patterns 
here im going to print pyramid pattern using astric
problem --> https://takeuforward.org/plus/dsa/problems/pattern-7?source=strivers-a2z-dsa-track


output --> 
Enter number of lines :5
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 


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
