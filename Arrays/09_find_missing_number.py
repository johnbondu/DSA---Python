Given an array arr[] of size n-1 with distinct integers in the range of [1, n]. This array represents a permutation of the integers from 1 to n with one element missing. Find the missing element in the array.

Examples: 

Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
Output: 6
Explanation: All the numbers from 1 to 8 are present except 6.

Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: Here the size of the array is 4, so the range will be [1, 5]. The missing number between 1 to 5 is 4

SOLUTIONS --->


def finding_missing_number(arr):
    n = len(arr)+1
    total = n* (n+1) //2
    sum_of_array =0
    for num in arr:
        sum_of_array +=num
    return total - sum_of_array
arr = list(map(int,input("Enter arr: ").split()))
print(finding_missing_number(arr))

OUTPUT ---->
Enter arr: 1 2 3 4 5 6 8
7

Complexity
Time	Space
Sum Formula	O(n)	O(1)
