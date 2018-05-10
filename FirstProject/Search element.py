'''Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 1:

Input: [1,3,5,6], 0
Output: 0'''

sorted_array = [1,3,5,8]
target = 6

def search_element():
    for i in range(0, len(sorted_array)):
        #print(sorted_array[i])
        if sorted_array[i] == target:
             print("Target at index: ",i)
             return i
    #
        elif sorted_array[i] > target:
             print("Add target at index: ", i)

             sorted_array.insert(i,target)
             print(sorted_array)
             return i



search_element()