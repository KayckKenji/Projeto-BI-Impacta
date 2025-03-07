**# Projeto-BI-Impacta**

Projeto de análise de dados

Este repositório contém um script em Python que gera uma base de dados fictícia para análise de vendas de suplementos. A base foi criada utilizando a biblioteca “Pandas” para simular um conjunto de dados realista.

**Tecnologias Utilizadas**

* Python
* Pandas
* NumPy (para geração aleatória avançada)
* random (para aleatoriedade básica)
  
**Como o Script Funciona**

O script gera um conjunto de dados fictícios contendo informações sobre vendas de suplementos. Os principais campos da base de dados incluem:
* Produto (exemplo: Whey Protein, Creatina, Pré-treino)
* Marca
* Preço
* Custo
* Região
* Data da venda
* Quantidade
* Faturamento
Os dados são gerados aleatoriamente dentro de um intervalo lógico para simular um cenário real de vendas.

**Aqui está o código utilizado para gerar a base de dados:**

# Importação das bibliotecas
```python
import pandas as pd
import numpy as np
from random import choice, uniform, randint
```
# Definição das categorias
```python
marcas = ["Growth", "Max Titanium", "Dark Lab", "Integral Médica", "Probiótica"]
produtos = ["Creatina", "Pré-Treino", "Whey", "Hiper Calórico", "BCAA"]
regioes = ["Sul", "Sudeste", "Centro-Oeste", "Nordeste", "Norte"]
```

# Tabela de custo fixo por marca e produto
```python
custos = {
    "Growth": {"Creatina": 50, "Pré-Treino": 70, "Whey": 90, "Hiper Calórico": 110, "BCAA": 60},
    "Max Titanium": {"Creatina": 55, "Pré-Treino": 75, "Whey": 95, "Hiper Calórico": 115, "BCAA": 65},
    "Dark Lab": {"Creatina": 60, "Pré-Treino": 85, "Whey": 100, "Hiper Calórico": 120, "BCAA": 70},
    "Integral Médica": {"Creatina": 52, "Pré-Treino": 72, "Whey": 92, "Hiper Calórico": 112, "BCAA": 62},
    "Probiótica": {"Creatina": 53, "Pré-Treino": 73, "Whey": 93, "Hiper Calórico": 113, "BCAA": 63}
}
```

# Função para gerar preço baseado na região
```python
def gerar_preco(marca, produto, regiao):
    base_price = custos[marca][produto] * uniform(1.2, 1.5)  # Margem de lucro de 20% a 50%
    ajuste_regiao = {"Sul": 0.95, "Sudeste": 1.0, "Centro-Oeste": 1.05, "Nordeste": 1.1, "Norte": 1.15}
    return round(base_price * ajuste_regiao[regiao], 2)
```
# Gerando os dados
```python
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
```
# Criando DataFrame
```python
df = pd.DataFrame(dados, columns=["Produto", "Marca", "Preço", "Custo", "Região", "Data da Venda", "Quantidade Vendida"])
df.head() # Exibir primeiras linhas
df = pd.DataFrame(dados)
```
# Salvar em um arquivo CSV
```python
csv_filename = "suplementos_powerbi.csv"
df.to_csv(csv_filename, index=False)

print(f"Arquivo gerado: {csv_filename}")
```
Dessa forma, o arquivo .csv com a base de dados é gerada na pasta do projeto

* Obs: 
Notamos que quando importamos os dados para o Power BI sao gerados alguns valores de “preco” menores que os valores de “custo”. Estamos providenciando o ajuste para este ponto. 
