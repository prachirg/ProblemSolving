def fact(n):
        result = 1
        for i in range(n, 0, -1):
            result = result * i
        return result

print(fact(3))


def recur_fact(n):
    if n == 0:
        return 1

    return recur_fact(n - 1) * n

print(recur_fact(4))

def recur_fibo(p):
    if p==0:
        return 0
    if p==1:
        return 1

    return recur_fibo(p-1)+recur_fibo(p-2)

print(recur_fibo(4))

def fibo(p):
    a = 0
    b = 1

    if p==0:
        return 0
    if p==1:
        return 1
    for i in range(2,p+1):
        c = a + b
        a = b
        b = c
    return c

print(fibo(6))

