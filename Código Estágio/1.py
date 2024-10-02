def Fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    elif i > 1:
        return (Fibonacci(i - 1)) + (Fibonacci(i - 2))


num = int(input("Insira número que deseja verificar se pertence a sequencia de Fibonacci: "))
k = 0
while Fibonacci(k) < num:
    k+=1
if Fibonacci(k) == num:
    print(f"O número {num} percente a sequencia de Fibonacci.")
else:
    print(f"O número {num} não percente a sequencia de Fibonacci")