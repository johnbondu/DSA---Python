problem -- > https://takeuforward.org/plus/dsa/problems/pattern-2?source=strivers-a2z-dsa-track
#secod pattern
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 


# here the logic is first loop runs for n lines and the 2nd  loop j runs i times for  in those lines 
n = int(input ("Enter number of lines :"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end =" ")
    print()
