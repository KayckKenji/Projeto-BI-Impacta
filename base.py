import pandas as pd
import numpy as np
from random import choice, uniform, randint

# Definição das categorias
marcas = ["Growth", "Max Titanium", "Dark Lab", "Integral Médica", "Probiótica"]
produtos = ["Creatina", "Pré-Treino", "Whey", "Hiper Calórico", "BCAA"]
regioes = ["Sul", "Sudeste", "Centro-Oeste", "Nordeste", "Norte"]

# Tabela de custo fixo por marca e produto
custos = {
    "Growth": {"Creatina": 50, "Pré-Treino": 70, "Whey": 90, "Hiper Calórico": 110, "BCAA": 60},
    "Max Titanium": {"Creatina": 55, "Pré-Treino": 75, "Whey": 95, "Hiper Calórico": 115, "BCAA": 65},
    "Dark Lab": {"Creatina": 60, "Pré-Treino": 85, "Whey": 100, "Hiper Calórico": 120, "BCAA": 70},
    "Integral Médica": {"Creatina": 52, "Pré-Treino": 72, "Whey": 92, "Hiper Calórico": 112, "BCAA": 62},
    "Probiótica": {"Creatina": 53, "Pré-Treino": 73, "Whey": 93, "Hiper Calórico": 113, "BCAA": 63}
}

# Função para gerar preço baseado na região
def gerar_preco(marca, produto, regiao):
    base_price = custos[marca][produto] * uniform(1.2, 1.5)  # Margem de lucro de 20% a 50%
    ajuste_regiao = {"Sul": 0.95, "Sudeste": 1.0, "Centro-Oeste": 1.05, "Nordeste": 1.1, "Norte": 1.15}
    return round(base_price * ajuste_regiao[regiao], 2)

# Gerando os dados
np.random.seed(42)  # Para reprodutibilidade
dados = []
for _ in range(50_000):
    marca = choice(marcas)
    produto = choice(produtos)
    regiao = choice(regioes)
    preco = gerar_preco(marca, produto, regiao)
    custo = custos[marca][produto]
    data_venda = pd.to_datetime("2024-01-01") + pd.to_timedelta(randint(0, 60), unit="D")  # Vendas entre janeiro e março
    quantidade = randint(1, 10)
    
    dados.append([produto, marca, preco, custo, regiao, data_venda, quantidade])

# Criando DataFrame
df = pd.DataFrame(dados, columns=["Produto", "Marca", "Preço", "Custo", "Região", "Data da Venda", "Quantidade Vendida"])

# Exibir primeiras linhas
df.head()

# Criar um DataFrame
df = pd.DataFrame(dados)

# Salvar em um arquivo CSV
csv_filename = "suplementos_powerbi.csv"
df.to_csv(csv_filename, index=False)

print(f"Arquivo gerado: {csv_filename}")