import pandas as pd

dados = {
    "Name": ["Pytherson", "Pip", "Pep"],
    "Account": [{"Number": "00001-1", "Agency": "0001", "Balance": "0.00", "limit": "500.00"},
                {"Number": "00002-2", "Agency": "0001", "Balance": "0.00", "limit": "500.00"},
                {"Number": "00003-3", "Agency": "0001", "Balance": "0.00", "limit": "500.00"}],
    "Card": [{"Number": "**** **** **** 1111", "limit": "1000.00"},
             {"Number": "**** **** **** 2222", "limit": "1000.00"},
             {"Number": "**** **** **** 3333", "limit": "1000.00"}]
}

df = pd.DataFrame(dados)
df.to_csv("SDW.csv")