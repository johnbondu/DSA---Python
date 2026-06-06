we have to increase and decrease the astric to get the correct pattern 
problem -->   https://takeuforward.org/plus/dsa/problems/pattern-10?source=strivers-a2z-dsa-track



output --> 


Enter number of lines :5
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

n=int(input("enter no.of lines: "))
#increasing part 
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()
#decreasing part
for i in range (n-1,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
# for the best way to write 
# n = int(input("Enter number of lines: "))

# # upper part
# for i in range(1, n + 1):
#     print("* " * i)

# # lower part
# for i in range(n - 1, 0, -1):
#     print("* " * i)
