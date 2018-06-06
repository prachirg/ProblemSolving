def bub_sort(list):
    temp = 0
    print(list)
    for pass1 in range(1,len(list)):
        #print("i:",i,list)
        for j in range(0,len(list)- pass1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
        print(pass1, j, list)
    return list

a  = [10,5,3,6,8,4]
print(bub_sort(a))

