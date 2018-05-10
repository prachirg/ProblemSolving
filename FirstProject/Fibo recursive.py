#0 1   1 2 3 5
def fibo(p):
    a = 0
    b = 1
    if p == 0:
        return a
    if p == 1:
        return b

    for i in range(2, p+1):
        c = a+b
        a = b
        b = c

    return c

#print(fibo(3))

def fibo(p):
            if p==0:
                print("p:",p)
                return 0

            if p==1:
                #print("2nd if p:",p)
                return 1

            if p>1:
                #print("3rd if p:", p)
                a = fibo(p-1)
                b = fibo(p-2)
                final_fibo = a + b
                print("fibo-1:",a , "fibo-2:", b, "final_fibo:", final_fibo)
                return final_fibo

print(fibo(4))




