import pandas as pd

class DataCleaner:
    """
    Uma classe para encapsular métodos de limpeza e transformação de dados
    de um DataFrame, promovendo modularidade e reutilização de código.
    
    Esta classe atua como uma API de processamento de dados, permitindo
    a orquestração de transformações via o método pipeline().
    """
    def __init__(self, df: pd.DataFrame, *args, **kwargs) -> None: 
        """
        Inicializa a classe com o DataFrame e armazena configurações adicionais.

        Parameters
        ----------
        df : pd.DataFrame
            O DataFrame de entrada para ser limpo e transformado.
        *args
            Argumentos posicionais variáveis, repassados.
        **kwargs
            Argumentos nomeados variáveis. Armazenados em self.config para
            configurações de pipeline (ex: limites, estratégias).
        """
        self.df = df
        self.args = args
        self.config = kwargs
        if self.config:
            print(f"Configurações adicionais carregadas: {self.config}")
        # print('DataCleaner inicializado.')
        print(f"DataCleaner inicializado com {len(self.df)} linhas.")
    
    def calcular_faturamento(self) -> pd.DataFrame: 
        """
        Calcula o faturamento total e adiciona a coluna 'faturamento' ao DataFrame.
        
        A operação utiliza List Comprehension para melhor performance.

        Returns
        -------
        pd.DataFrame
            O DataFrame interno (self.df) com a nova coluna 'faturamento' adicionada.
        """
        self.df['faturamento'] = [
            preco*quantidade for preco, quantidade in zip(
            self.df['preco_unitario'], self.df['quantidade_vendida']
            )]
        return self.df
    
    def pipeline(self) -> pd.DataFrame:
        '''
        Executa o pipeline completo de limpeza e transformação de dados.

        Este método orquestra a chamada sequencial de todos os métodos
        de transformação do DataCleaner.

        Returns
        -------
        pd.DataFrame
            O DataFrame final após todas as etapas de processamento.
        '''
        self.calcular_faturamento()
        print("— Faturamento calculado.")
        return self.df
    
    @classmethod
    def from_csv(cls, caminho_arquivo: str, *args, **kwargs) -> 'DataCleaner':
        """
        Cria uma nova instância de DataCleaner a partir de um arquivo CSV (Construtor Alternativo).

        Parameters
        ----------
        caminho_arquivo : str
            Caminho para o arquivo CSV a ser carregado.
        *args
            Argumentos posicionais repassados para o __init__.
        **kwargs
            Argumentos nomeados repassados para o pd.read_csv (ex: 'encoding')
            e, em seguida, para o __init__ (para configurar o self.config).

        Returns
        -------
        DataCleaner
            Uma nova instância da classe DataCleaner com o DataFrame carregado.
        """
        # utiliza o pop() para extrair o encoding (caso exista). Se não existir, usa None ou 'utf-8' como padrão.
        encoding_csv = kwargs.pop('encoding', 'utf-8')

        # repassa apenas o 'encoding' para o pd.read_csv
        df = pd.read_csv(caminho_arquivo, encoding = encoding_csv)

        # repassa os outros args e kwargs para que o __init__ possa utilizá-los
        return cls(df, *args, **kwargs)
    
    @staticmethod
    def converter_para_milhares(valor: float) -> float:
        """
        Converte um valor monetário em sua representação em milhares.

        Parameters
        ----------
        valor : float
            O valor numérico a ser convertido.

        Returns
        -------
        float
            O valor dividido por 1000, arredondado para três casas decimais.
        """
        return round(valor/1000, 3) # converte para milhares com 3 casas decimais
    