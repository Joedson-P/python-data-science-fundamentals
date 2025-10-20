import pandas as pd
import numpy as np

# Definindo o número de linhas para a simulação de volume
NUM_LINHAS = 500000

# Dados de simulação
produtos = [f'Produto_{i}' for i in range(1000)]
categorias = ['Eletronicos', 'Livros', 'Roupas', 'Alimentos', 'Servicos']

# Criação do DataFrame simulado
data = {
    'produto': np.random.choice(produtos, NUM_LINHAS),
    'preco_unitario': np.random.uniform(10.0, 500.0, NUM_LINHAS).round(2),
    'quantidade_vendida': np.random.randint(10, 2000, NUM_LINHAS),
    'categoria': np.random.choice(categorias, NUM_LINHAS)
}

df_produtos = pd.DataFrame(data)

# Salvar o DataFrame para uso no Notebook
# Salvo na pasta /data para fácil acesso e organização
df_produtos.to_csv('data/df_produtos_500k.csv', index=False)

print(f"DataFrame 'df_produtos' criado e salvo com {len(df_produtos)} linhas em /data/df_produtos_500k.csv.")