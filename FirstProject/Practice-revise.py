#fibonacci

def fibo(n):
    a=0
    b=1
    if n==0:
        return a

    if n==1:
        return b

    if n>1:
        return fibo(n-1)+fibo(n-2)

#print(fibo(3))

def fibonacci(p):
    a =0
    b = 1
    for i in range(0,p):
        print(a)
        a, b = b, a+b

#fibonacci(9)

def fact(n):
    factorial = 1
    for i in range(n, 1, -1):
        factorial = factorial * i
    return factorial

#print(fact(4))

def facto(n):
    fact = 1
    if n==0:
        return fact
    if n>0:
        return facto(n-1)*n

#print(facto(3))

#Bubble sort  - [5,8,3,4,2]

def bub_sort(arr):
    temp = 0
    for pas in range(1,len(arr)):
        for i in range(0,len(arr)-pas):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr

a = [5,8,3,4,2]
#print(bub_sort(a))

#merge sort

def merge(arr, low, mid, high):







