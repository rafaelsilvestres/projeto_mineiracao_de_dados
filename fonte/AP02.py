import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

atributos = ["C008", "Q06306"]
df = pd.read_csv("pns2019.csv", usecols = atributos) #Ler base de dados

df.columns = ["idade", "tem_doencas_do_coracao"] # Muda o nome das colunas 

df_doentes = df[df["tem_doencas_do_coracao"] == 1] # Cria um df somente com os doentes de coracao

df_doentes["idade"].describe() #Ver minimo e máximo da idade
df_doentes.info()

# Tabela de Frequência -----------------------------------------------
k = 1 + 3.322 * np.log10(4732) #definir o numero de classes
k = int(k)
minimo = 15
maximo = 104
a = maximo - minimo 
h = a/k
h = round(h)

faixas = pd.cut(df_doentes["idade"], np.arange(15, 107, h), right = False) # array([ 15,  22,  29,  36,  43,  50,  57,  64,  71,  78,  85,  92,  99, 106])
contagem = faixas.value_counts()
contagem = contagem.sort_index()

tabela_frequencia = pd.DataFrame()
tabela_frequencia["Intervalos"] = contagem.index.astype(str)
tabela_frequencia["fi"] = contagem.values
tabela_frequencia["fr"] = contagem.values / 4732 
tabela_frequencia["Fi"] = contagem.values.cumsum() 
tabela_frequencia["Fr"] = tabela_frequencia["fr"].cumsum()

print(tabela_frequencia)

# Gráfico Frequencia Relativa Acumulada ---------------------------

x = np.arange(15, 107, h)
y = [0] + list(tabela_frequencia["Fr"])

plt.figure(figsize = (12,6))
sns.lineplot(x = x, y = y, marker="o")
plt.xlabel("Faixas de Idade")
plt.ylabel("Frequência Relativa Acumulada")
plt.title("Pessoas com doenças do coração por idade (PNS 2019)")
plt.grid(alpha=0.3)
plt.xticks(x)
plt.show()



