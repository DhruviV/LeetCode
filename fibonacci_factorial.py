n=4
fact=1
def fibo(n):
    if n<=1:
        return n
    else:
        return (fibo(n-1)+ fibo(n-2))


# fibo(n)
# for i in range(n):
#     print(fibo(i))
def factorial(n,fact):
    for i in range(1,n+1):
        fact = fact*i
    print(fact)
factorial(n,fact)