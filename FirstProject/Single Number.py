'''Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?'''

a = [1,2,3,4,1,2,3,1]
#b=set(a)
# print(b)
# for i in range(0, len(a)):
#     if a.count(a[i])==1:
#         print(a[i])
#b=(1,2,3,4)
#count=0

#time complexity = n2
# for e in b:
#     for i in range(0,len(a)-1):
#         #print(e)
#         if a[i] == e:
#             count=count+1
#     #print("e:",e,"count",count)
#     if count == 1:
#         print(e)
#         print("count")

            #print("J:", a[j], "count:", count)
    #print("Outer for loop")
#    count=0


# print(b.add(4))
# print(b)

#time complexity = n
pre_length=0
post_length=0
b = dict()

for new in range(0, len(a)-1):
    if b.get(a[new]) == None :
        #print("True")
        b.update({a[new]:False})
    else:
        b.update({a[new]:True})

for k, v in b.items():
    if v == False:
        print(k)

#O(2n)= n = linear
#O(n^2) =n^2 = non-linear



