import pytest
import pandas as pd
from src.datacleaner import DataCleaner # <-- Importando a classe a ser testada

@pytest.fixture
def sample_dataframe():
    '''Cria um DataFrame de amostra para testes unitários'''
    data = {
        'id_produto': [1, 2, 3, 4],
        'preco_unitario': [10.0, 20.0, 5.0, 15.0],
        'quantidade_vendida': [2, 5, 1, 10],
        'categoria': ['A', 'B', 'A', 'C']
    }

    return pd.DataFrame(data)

# --- Testando a inicialização e métodos básicos ---

def test_data_cleaner_inicialization(sample_dataframe):
    '''Verifica se o construtor da classe DataCleaner funciona corretamente'''
    # AÇÃO (ACT): Instancia a classe
    cleaner = DataCleaner(sample_dataframe.copy())

    # VERIFICAÇÃO (ASSERT): Verifica se o DataFrame foi armazenado e tem o tamanho correto
    assert cleaner.df.shape[0] == 4
    assert 'id_produto' in cleaner.df.columns

def test_converter_para_milhares_staticmethod():
    '''Verifica se o método estático de conversão funciona corretamente'''
    # CENÁRIO (GIVEN): Valores de teste
    valor = 456231.98

    # AÇÃO (ACT): Chama o método estático diretamente pela classe
    resultado = DataCleaner.converter_para_milhares(valor)

    # VERIFICAÇÃO (ASSERT): O valor esperado é 456.232 (arredondado para 3 casas decimais)
    assert resultado == 456.232
    assert isinstance(resultado, float)

def test_calcular_faturamento_logic(sample_dataframe):
    '''
    Verifica se o método calcular_faturamento calcula a coluna 'faturamento' corretamente.
    Faturamento Esperado: [10*2, 20*5, 5*1, 15*10] = [20.0, 100.0, 5.0, 150.0]
    '''
    # CENÁRIO (GIVEN): Instancia o DataCleaner com uma cópia do df de amostra
    cleaner = DataCleaner(sample_dataframe.copy())

    # AÇÃO (WHEN): Executa o método de transformação
    cleaner.calcular_faturamento()

    # VERIFICAÇÃO 1 (THEN): Verifica se a nova coluna 'faturamento' foi criada
    assert 'faturamento' in cleaner.df.columns

    # VERIFICAÇÃO 2 (THEN): Verifica se a lógica de cálculo está correta
    faturamento_esperado = pd.Series([20.0, 100.0, 5.0, 150.0])

    #Comparação dos valores calculados com os esperados (utilizando allclose para segurança com floats)
    pd.testing.assert_series_equal(
        cleaner.df['faturamento'],
        faturamento_esperado,
        check_names = False,
        atol = 1e-5
    )