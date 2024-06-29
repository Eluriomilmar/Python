def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [4, 5, 7, 2, 1]
dobra(valores)
print(valores)