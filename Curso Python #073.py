#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.
colocacao = ("Flamengo", "Palmeiras", "São Paulo", "Athletico Paranaense", "Atlético Mineiro", "Corinthians", "Fluminense", "Grêmio", "Fortaleza", "América Mineiro", "Internacional", "Santos", "Bahia", "Botafogo", "Red Bull Bragantino", "Atlético Goianiense", "Cruzeiro", "Ceará", "Cuiabá", "Goiás")
print(f"Os 5 primeiros times foram: {colocacao[0:5]}")
print(f"Os últimos 4 colocados foram: {colocacao[-4]}")
print(f"Os times em ordem alfabética são: {sorted(colocacao)}")
print(f"O chapecoense está na posição: {"chapecoense" in colocacao}")