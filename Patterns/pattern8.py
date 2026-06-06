Here the pattern and formula was same but we reverse the pyramid pattern 

problem -->  https://takeuforward.org/plus/dsa/problems/pattern-8?source=strivers-a2z-dsa-track


Enter number of lines :4
* * * * * * * 
  * * * * * 
    * * * 
      * 


n = int(input ("Enter number of lines :"))
for i in range(n,0,-1):
    #for space 
    for j in range(n-i):
        print(" ",end=" ")
    #for pyramid
    for k in range(2*i-1):
        print("*",end=" ")
    #for extra line 
    print( )
