'''Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].'''
nums=[0, 0, 1, 3, 12]
#nums=[1, 3, 12, 0]


# from collections import deque
# nums = deque([0, 1, 0, 3, 12])
#
# def move_zero():
#     for i in range(0, len(nums)):
#         if nums[i] == 0:
#         #    return
#
#         nums.popleft()
#     print(nums)
#
#
# move_zero()
i=0
while(i < len(nums)):
    print("nums i:",i)
    if nums[i]==0:
        print("removing..",i)
        nums.remove(nums[i])
        print("i:",i,"after remove:",nums)
        nums.append(0)
    i = i + 1
    print("i:",i,"after:",nums)



