
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

a = [3,6,8,10,15,20,25]
print(search_num(10, 0, len(a)-1, a))





