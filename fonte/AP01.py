import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leitura da base de dados
atributos = ["V0001", "C008", "Q06306"]
df = pd.read_csv("pns2019.csv", usecols = atributos)

df.columns = ["uf", "idade", "tem_doencas_do_coracao"] # Altera o nome das colunas

# Cria nova base de dados somente com idosos
df_idosos = df.drop(df[df["idade"] < 60].index)
df_idosos = df_idosos.dropna(subset = ["idade"])

# Tratar a coluna uf
df_idosos.info()
ufs = {
    11: "RO", 12: "AC", 13: "AM", 14: "RR", 15: "PA",
    16: "AP", 17: "TO", 21: "MA", 22: "PI", 23: "CE",
    24: "RN", 25: "PB", 26: "PE", 27: "AL", 28: "SE",
    29: "BA", 31: "MG", 32: "ES", 33: "RJ", 35: "SP",
    41: "PR", 42: "SC", 43: "RS", 50: "MS", 51: "MT",
    52: "GO", 53: "DF"
}
df_idosos["uf_decod"] = df_idosos["uf"].map(ufs)

# Visualização ----------------------------------------------------
# Contagem absoluta
df_idosos_doentes = df_idosos[df_idosos["tem_doencas_do_coracao"] == 1].copy() # Cria um df com somente tem_doencas_do_coracao == 1
df_idosos_doentes.info()

contagem = df_idosos_doentes["uf_decod"].value_counts(ascending=True) # conta quantos casos tem em cada estado

plt.figure(figsize=(12, 6))
sns.countplot(data = df_idosos_doentes, x="uf_decod", order=contagem.index)
plt.title("Contagem absoluta de doenças do coração em idosos, por estado (PNS 2019)")
plt.xlabel("Estado")
plt.ylabel("Número de casos")
plt.show()

# Contagem relativa
r_total = df_idosos.groupby("uf_decod").size()
r_casos = df_idosos_doentes.groupby("uf_decod").size()
relativo = (r_casos / r_total)*100
relativo = relativo.sort_values(ascending = True)

plt.figure(figsize=(12, 6))
sns.barplot(x = relativo.index, y = relativo.values)
plt.title("Contagem relativa de doenças do coração em idosos, por estado (PNS 2019)")
plt.xlabel("Estado")
plt.ylabel("% de idosos com a doença")
plt.show()