problem statement ------>

Given an array of nums of n integers. Every integer in the array appears twice except one integer. Find the number that appeared once in the array.


Example 1

Input : nums = [1, 2, 2, 4, 3, 1, 4]

Output : 3

Explanation : The integer 3 has appeared only once.

Example 2

Input : nums = [5]

Output : 5

Explanation : The integer 5 has appeared only once.

solution ----> 


  def getSingleElement(arr):
    freq ={ }
    for i in arr:
        freq[i] = freq.get(i,0)+1
    
    for key in freq:
        if freq[key] ==1:
            return key
            
arr = [1, 2, 2, 4, 3, 1, 4]
print(getSingleElement(arr))

 output ------->
3

#here  in this array we have only 3 appears one time so we have to return that element
  
