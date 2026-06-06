# Here the pattern is differnt  from the last patterns 
#here we dcrease the order of n 
problem --> https://takeuforward.org/plus/dsa/problems/pattern-5?source=strivers-a2z-dsa-track


output    
Enter number of lines :5
* * * * * 
* * * * 
* * * 
* * 
* 

n = int(input ("Enter number of lines :"))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end = " ")
    print()
