import json

media = 0
contador = 0
maior = float("-inf")
menor = float("+inf")
with open("dados.json", "r") as arquivo:
    vetor = json.load(arquivo)
    for i in vetor:
        if i.get("valor") > 0:
            media += i.get("valor")
            contador += 1
            if maior < i.get("valor"):
                maior = i.get("valor")
            if menor > i.get("valor"):
                menor = i.get("valor")
    media = media/contador
    contador = 0 #estou reutilizando avariável pois a mesma se tornou obsoleta
    for i in vetor:
        if i.get("valor") > media:
            contador += 1
    print(f"O menor faturamento foi de: {menor}\n"
          f"O maior faturamento foi de: {maior}\n"
          f"Houveram {contador} dias onde o faturamento foi maior que a média de {media:.4f}")
