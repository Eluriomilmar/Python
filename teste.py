def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * (fatorial(n-1))



n = fatorial(5)

print(f"o dobro do número é igual a {n}")