def merge_sort(a_list, low, high):
    if low<high:
        mid = int((low+high)/2)
        merge_sort(a_list, low, mid) #left half
        merge_sort(a_list, mid+1, high) #right half
        merge(a_list, low, mid, high)

def merge(a_list, low, mid, high):
    c = [item for item in a_list]
    #print(c)
    i = low
    j = mid+1
    k = low #apni hi duniya mein hai c
    while(i<=mid and j<=high):
        if a_list[i]<=a_list[j]:
            c[k]=a_list[i]
            k+=1
            i+=1
        else:
            c[k]=a_list[j]
            k+=1
            j+=1

    for x in range(i, mid+1):
        c[k]=a_list[x]
        k+=1

    for y in range(j, high+1):
        c[k]=a_list[y]
        k+=1

    for z in range(low, high+1):
        a_list[z]=c[z]

    print(c)

a=[1, 6, 8, 2, 5, 7, 10, 1, 2]
#  0  1  2  3  4  5  6   7  8
#             low    mid    high
# c = [1, 2, 5, 7, 10]
#      0  1  2  3  4

# Sureshan
# c[1, 6, 8, 2, 5, 7, 10, 1, 2]

# c[1, 6, 8, 2, 1, 2, 5, 7, 10]


print(merge_sort(a, 0, len(a)-1))