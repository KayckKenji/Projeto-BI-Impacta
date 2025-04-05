import pandas as pd
import numpy as np
from random import choice, randint, uniform

# Listas fixas
marcas = ["Growth", "Max Titanium", "Dark Lab", "Integral Médica", "Probiótica"]
produtos = ["Creatina", "Pré-treino", "Whey", "Hiper Calórico", "BCAA"]
regioes_ufs = {
    "Sul": ["RS", "SC", "PR"],
    "Sudeste": ["SP", "RJ", "MG", "ES"],
    "Centro-Oeste": ["GO", "MT", "MS", "DF"],
    "Nordeste": ["BA", "PE", "CE", "RN", "PB", "MA", "AL", "SE", "PI"],
    "Norte": ["AM", "PA", "RO", "RR", "TO", "AC", "AP"]
}

# Custo fixo por marca e produto
custos = {
    "Growth": {"Creatina": 50, "Pré-treino": 70, "Whey": 90, "Hiper Calórico": 110, "BCAA": 60},
    "Max Titanium": {"Creatina": 55, "Pré-treino": 75, "Whey": 95, "Hiper Calórico": 115, "BCAA": 65},
    "Dark Lab": {"Creatina": 60, "Pré-treino": 85, "Whey": 100, "Hiper Calórico": 120, "BCAA": 70},
    "Integral Médica": {"Creatina": 52, "Pré-treino": 72, "Whey": 92, "Hiper Calórico": 112, "BCAA": 62},
    "Probiótica": {"Creatina": 53, "Pré-treino": 73, "Whey": 93, "Hiper Calórico": 113, "BCAA": 63}
}

# Ajustes por região
ajuste_regiao = {
    "Sul": 1.02,
    "Sudeste": 1.3,
    "Centro-Oeste": 1.05,
    "Nordeste": 1.1,
    "Norte": 1.15
}

# Gerador de dados
np.random.seed(42)  # Reprodutibilidade
dados = []

for _ in range(50000):
    marca = choice(marcas)
    produto = choice(produtos)
    custo = custos[marca][produto]
    regiao = choice(list(regioes_ufs.keys()))
    uf = choice(regioes_ufs[regiao])
    margem_lucro = uniform(1.2, 1.5)
    preco_base = custo * margem_lucro * ajuste_regiao[regiao]
    preco_final = round(preco_base, 2)
    quantidade = randint(1, 10)
    faturamento = round(preco_final * quantidade, 2)
    data_venda = pd.to_datetime("2024-01-01") + pd.to_timedelta(randint(0, 60), unit="D")

    dados.append([
        produto,
        marca,
        custo,
        round(margem_lucro, 2),
        preco_final,
        quantidade,
        faturamento,
        data_venda.date(),
        "Brasil",
        regiao,
        uf
    ])

# Criar DataFrame
colunas = [
    "Produto", "Marca", "Custo", "Margem de Lucro", "Preço Final",
    "Quantidade Vendida", "Faturamento", "Data da Venda", "País", "Região", "UF"
]

df = pd.DataFrame(dados, columns=colunas)

# Salvar em Excel
nome_arquivo = "vendas_suplementos_base.xlsx"
df.to_excel(nome_arquivo, index=False)

print(f"Base de dados gerada com sucesso: {nome_arquivo}")
