def fact_recur(n):
    if n == 0:
        return 1
    else:
        return n*fact_recur(n-1)

#print(fact_recur(4))

def fact(n):
    factorial = 1
    if n == 0:
        return 1
    else:
        for i in range(n, 0, -1):
            factorial=factorial*(i)

        print(factorial)

fact(0)

