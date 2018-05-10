'''Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2'''

n = [2,2,1,1,1,2,2]
s = set(n)
def count(e):
    total_count=0
    for i in range(0,len(n)):
        if n[i]==e:
            total_count+=1
    return total_count

def majority_ele():
    element_count = int(len(n)/2)
    for i in s:
        if count(i) > element_count:
            return i


print(majority_ele())






