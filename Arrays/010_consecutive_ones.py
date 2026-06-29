problem statement ------>   Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.


  Solutions ---->
  def consecutive_ones(arr1):
    count = 0
    max_len = 0
    for i in range(len(arr1)):
        if arr1[i] == 1:
            count +=1
        else:
            count =0
        max_len = max(max_len,count)
        
    return max_len   
arr1 = [1,1,0,1,1,1]       
print(consecutive_ones(arr1))



output ------>
3
#because here we have 1,1,1
