def Fibo(n):
    if n <= 1: return n
    return Fibo(n-2) + Fibo(n-1)

for i in range(8): print(Fibo(i))