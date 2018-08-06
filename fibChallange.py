def fib(n):
    a = 1
    b = 1
    temp = 0
    fibonachi = []
    while b <= n:
        temp = a
        a = a+b
        fibonachi.append(temp)
        fibonachi.append(b)
        
        b = b+a
    print(fibonachi)
