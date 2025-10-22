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
    
    def pipeline(self):
        '''
        Executa o pipeline completo de limpeza e transformação de dados
        '''
        self.calcular_faturamento()
        print("— Faturamento calculado.")
        return self.df
    
    @classmethod
    def from_csv(cls, caminho_arquivo: str, *args, **kwargs):
        '''
        Cria uma instância de DataCleaner a partir de um arquivo CSV
        '''
        #Utilizando o pop() para extrair o encoding (caso exista). Se não existir, usa None ou 'utf-8' como padrão.
        encoding_csv = kwargs.pop('encoding', 'utf-8')

        # repassa apenas o 'encoding' para o pd.read_csv
        df = pd.read_csv(caminho_arquivo, encoding = encoding_csv)

        # repassa os outros args e kwargs para que o __init__ possa utilizá-los
        return cls(df, *args, **kwargs)
    
    @staticmethod
    def converter_para_milhares(valor):
        return round(valor/1000, 3) # converte para milhares com 3 casas decimais
    