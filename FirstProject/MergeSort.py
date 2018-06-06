def merge(a_list, low, mid, high):
    c = []
    i = low
    j = mid+1
    while(i<=mid and j<=high):
        if a_list[i] <= a_list[j]:
            #print('before i', i)
            c.append(a_list[i])
            i+=1
            #print('after i',i)
        else:
            #print('before j', j)
            c.append(a_list[j])
            j+=1
            #print('After j',j)
    #print("i:",i,"j:",j)
    #return c

    #bacha kucha
    for x in range(i,mid+1):
        c.append(a_list[x])
    #
    for y in range(j,high+1):
        c.append(a_list[y])

    return c

#a = [5,10,15,20]
b = [2,8,10,20,1,25,30]
print(merge(b, 0, 3, 6))

