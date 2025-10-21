import pandas as pd
import numpy as np

'''
Uma classe para encapsular métodos de limpeza e transformação de dados
de um DataFrame, promovendo modularidade e reutilização de código
'''
class DataCleaner:
    def __init__(self, df: pd.DataFrame, *args, **kwargs):
        self.df = df
        self.args = args
        self.config = kwargs
        if self.config:
            print(f"Configurações adicionais carregadas: {self.config}")
        # print('DataCleaner inicializado.')
        print(f"DataCleaner inicializado com {len(self.df)} linhas.")
    
    def calcular_faturamento(self):
        """
        Calcula o faturamento total (preco * quantidade) usando List Comprehension e adiciona a coluna faturamento.
        """
        self.df['faturamento'] = [
            preco*quantidade for preco, quantidade in zip(
            self.df['preco_unitario'], self.df['quantidade_vendida']
            )]
        return self.df