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

a = [5,8,3,4,2,9,9,1,1]
#print(bub_sort(a))

# b = set(a)
# print(b)
# a.sort(key=lambda x: x%3, reverse=True)
# print(a)

# for i in range(10, 0, -2):
#     if i%4==0:
#         print("divisible by 4:",i)
#         continue
#     print("not divisible",i)

#list comprehensions

# example = [x**2 for x in range(10)]
# #print(example)
# ex = list(map(lambda x: x**2,range(10)))
# #print(ex)
# test = [(x,y) for x in range(5) for y in range(5) if x!=y and x>y]
# print(test)

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
vec2=[x*2 for x in vec]
print(vec2)
# filter the list to exclude negative numbers
vec3=[x for x in vec if x>=0]
print(vec3)
# apply a function to all the elements
vec4 = [abs(x) for x in vec]
print(vec4)
# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
ff = [x.strip() for x in freshfruit]
print(ff)
# create a list of 2-tuples like (number, square)
tup = [(x, x**2) for x in vec]
print(tup)
# the tuple must be parenthesized, otherwise an error is raised
# tup = [x, x**2 for x in vec]
# print(tup)

# flatten a list using a listcomp with two 'for'
nested_list=[[1,2,3],[4,5]]
flatten = [y for x in nested_list for y in x]
print(flatten)

#set practice
# set_vec = set(vec)
# print(set_vec)
# set_ff = set(ff)
# print(set_ff)
# for i in set_vec:
#     print(i)

#dictionary practice
# i = sum = 0
#
# while i <= 4:
#     sum += i
#     i = i+1
#
# # print(sum)
# for char in 'PYTHON STRING':
#     if char == ' ':
#         break
#
#     print(char, end='')
#
#     if char == 'O':
#         continue

result = lambda x: x * x
print(result(5))







