'''
Fibonacci Series: 0, 1, 1, 2, 3, 5, 8, 13, 21,
Fibonacci Index, p:  0, 1, 2, 3, 4, 5, 6,  7,  8,

Write a function to return the Fibonacci number given the position, p
'''

def Fibonacci(p):
    #print("Hi")
    a = 0
    b = 1

    for i in range(0,p):
        a,b = b, a+b
    print(a)
    #print("HI")

Fibonacci(3)



'''
Your aim is to retrieve k nearest neighbor points to the point of interest, p

Input point: p
Sample points: 1, 2, .., n

k <= n

Assume distance between points is defined via the following function (interface):

def get_distance(p1, p2):
    distance_p1_p2 = ...
return distance_p1_p2

Write a function to return k nearest neighbors to p.

'''


# def nearest(p,k):
#
#     for i in range(1,n):
#         if k<
#         get_distance(p,i)
#     return



