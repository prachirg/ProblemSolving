
def search_num(target, low, high, list):
    if low>high:
        return -1, "Not found"
    mid = int((low+high)/2)
    if list[mid] == target:
        return mid
    if list[mid] < target:
        return search_num(target, mid+1, high, list) #shifting right
    if list[mid] > target:
        return search_num(target,low, mid-1, list) #shifting left

# a = [3,6,8,10,15,20,25]
#print(search_num(10, 0, len(a)-1, a))


# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 #low                          high
 #            low              high
 #              found target

 #Iterative
def bin_search(low, high, target, list):
    while(low <= high):
        mid = int((low+high)/2)
        if a[mid] == target:
            return a[mid]
        elif a[mid] < target:
            low = mid + 1
        elif a[mid] > target:
            high = mid - 1
        else:
            return "Not found"
    return "Not found"

a = [3,6,8,10,15,20,25]
print(bin_search(0, len(a)-1, 21, a))