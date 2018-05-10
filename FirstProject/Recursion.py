# a=0
# b=1
#
# def fib(a,b):
#     if a < 20:
#         print(a)
#         a, b = b, a+b
#         fib(a,b)

#fib(0,1)

def fact():
    a = 1
    for i in range(3, 1, -1):
        #print(i)
        a = i*a

    print(a)

#fact()

def factorial(a):
    if a == 0:
        return 1
    else:
        i = a*(factorial(a-1))

        return(i)
    #print(i)

print(factorial(3))
