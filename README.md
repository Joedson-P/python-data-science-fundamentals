# 🐍 Projeto de Engenharia de Código em Python: Otimização e Modularidade

## 💡 Descrição do Projeto
Este projeto serve como uma demonstração prática dos fundamentos de Data Science, aplicando Arquitetura de Software Sólida para garantir performance e manutenibilidade. O objetivo principal é resolver o desafio de processar grandes volumes de dados (Large DataFrames) de forma lenta, aplicando as melhores práticas de Engenharia de Código Python e Programação Orientada a Objetos (POO).

## 🗂️ Estrutura do Repositório

O projeto segue uma estrutura profissional para separação de preocupações:

* `/data`: Contém o DataFrame de 500k linhas usado para benchmarking.
* `/src`: Contém a lógica de negócio encapsulada (`datacleaner.py`).
* `/notebooks`: Contém os Notebooks que demonstram e validam a performance e a arquitetura do código.

## 🚀 Como Executar

Para replicar a análise e testar a arquitetura modular:

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/Joedson-P/python-data-science-fundamentals.git
    cd python-data-science-fundamentals
    ```
2.  **Crie e Ative o Ambiente Virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    .\venv\Scripts\activate   # Windows
    ```
3.  **Instale as Dependências:**
    ```bash
    pip install pandas jupyter
    ```
4.  **Execute a Demonstração:**
    Abra e execute sequencialmente o Notebook: `/notebooks/2_modularidade_poo.ipynb` para ver a validação de performance e a arquitetura da classe `DataCleaner`.

## ⭐ Destaques Técnicos

A arquitetura do `DataCleaner` foi desenvolvida com foco em Manutenibilidade e Escalabilidade:

| Conceito | Aplicação |
| :--- | :--- |
| **Otimização Pythonic** | Uso de **List Comprehension** para calcular o faturamento, superando a performance de loops explícitos e métodos `apply()/map`. |
| **Modularidade (POO)** | Criação da classe `DataCleaner` no módulo `/src`, promovendo o Encapsulamento do estado (`self.df`) e a Separação de Preocupações. |
| **Design de Pipeline** | Implementação do método `pipeline()` para orquestrar a execução sequencial das transformações em uma única chamada de API. |
| **Extensibilidade** | Uso de `*args` e `**kwargs` no construtor e no `@classmethod` para aceitar configurações de processamento variáveis e não obrigatórias. |
| **API Avançada** | Implementação de `@classmethod` (construtor alternativo `from_csv`) e `@staticmethod` (função utilitária) para melhor usabilidade. |
| **Padronização** | Uso de **Type Hinting** e **Docstrings no Padrão NumPy Style** em toda a classe para clareza e geração automática de documentação. |
