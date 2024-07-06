def fib(n):
    a = 0
    while True:
        if n == 0:
            return 0
        if n == 1:
            return [0, 1]
        if a == 0:
            l = []
            l.append(a)
            a += 1
        if a == 1:
            l.append(a)
            a += 1
        else:
            l.append((l[len(l)-2]) + (l[len(l)-1]))
            a += 1
        if a == n:
            return l



def inteiro():
    while True:
        try:
            a = int(input("Em quantos passos deseja calcular Fibonacci?  "))
            if a < 0:
                raise ValueError
        except:
            print("Insira número inteiro e positivo.")
        else:
            return a


print(fib(inteiro()))