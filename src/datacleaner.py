import pandas as pd
import logging
import os
from dotenv import load_dotenv

# ----------------------------------------
# Carregar Variáveis de Ambiente do .env
# ----------------------------------------
load_dotenv()

# ----------------------------------------
# Configuração Padrão do Logging (INFO para produção)
# Configuração global para este módulo, formatando a saída com data/hora e nível.
# ----------------------------------------
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')
logger = logging.getLogger(__name__)

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
            logger.info(f"Configurações adicionais carregadas: {self.config}")
        logger.info(f"DataCleaner inicializado com {len(self.df)} linhas.")
    
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
        logger.info("— Faturamento calculado.")
        return self.df
    
    @classmethod
    def from_csv(cls, pasta_dados: str = 'data', *args, **kwargs) -> 'DataCleaner':
        """
        Cria uma nova instância de DataCleaner a partir de um arquivo CSV (Construtor Alternativo).

        Parameters
        ----------
        pasta_dados : str, opcional
            Caminho do diretório onde o arquivo de dados (definido em DATA_FILE_NAME no .env) está localizado. 
            O valor padrão é 'data'.
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

        # tenta carregar o nome do arquivo a partir da variável de ambiente
        file_name = os.getenv("DATA_FILE_NAME")

        if not file_name:
            logger.error("A variável 'DATA_FILE_NAME' não foi encontrada no ambiente.")
            raise EnvironmentError("DATA_FILE_NAME é obrigatória para o from_csv")
        
        # constrói o caminho completo do arquivo: pasta_dados/file_name
        caminho_completo = os.path.join(pasta_dados, file_name)

        logger.info(f"Tentando carregar dados de: {caminho_completo}")

        try:
            # utiliza o caminho completo e a lógica de encoding para ler o CSV
            df = pd.read_csv(caminho_completo, encoding = encoding_csv)
            logging.info("Dados carregados com sucesso")
        except FileNotFoundError:
            logger.error(f"Arquivo não encontrado no caminho: {caminho_completo}")
            raise FileNotFoundError(f"Verifique se o arquivo '{file_name}' está em '{pasta_dados}'.")

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
    