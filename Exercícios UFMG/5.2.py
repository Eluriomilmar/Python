#Faça uma função em Python para calcular a função harmônica
#com sinais alternados.

harm = float(input("Insira até qual termo deseja calcular a série harmônica: "))

def calc_harm(i):
    if i == 1:
        return 1
    else:
        if i%2 == 0:
            return -1*(1/i) + calc_harm(i-1)
        else:
            return (1/i) + calc_harm(i-1)

print("O valor da série harmônica é de: %f" % calc_harm(harm))