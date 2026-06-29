problem statement --- >  Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. The elements in the union must be in ascending order.



The union of two arrays is an array where all values are distinct and are present in either the first array, the second array, or both.


Example 1

Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]

Output: [1, 2, 3, 4, 5, 7]

Explanation:

The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2


solution --> 
def union_of_sorted_arr(arr1,arr2):
    union = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i+=1
        elif arr1[i] > arr2[j]:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j+=1
        else:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i+=1
            j+=1
    while i < len(arr1):
        if not union or union[-1] != arr1[i]:
            union.append(arr1[i])
        i+=1
    while j < len(arr2):
        if not union or union[-1] != arr2[j]:
            union.append(arr2[j])
        j+=1
    return union
    

arr1= list(map(int,input("Enter array1: ").split()))
arr2= list(map(int,input("Enter array2: ").split()))
print(union_of_sorted_arr(arr1,arr2))


OUTPUT --->
Enter array1: 1 2 3 4 5
Enter array2: 1 2 7
[1, 2, 3, 4, 5, 7]

Time Complexity
O(n + m)
Space Complexity
O(n + m) (to store the union array)
  
