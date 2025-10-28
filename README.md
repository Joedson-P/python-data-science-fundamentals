# 🐍 DataCleaner Project: Engenharia de Software para Data Science

## 💡 Descrição do Projeto
Este projeto demonstra a **Engenharia de Software de Produção** aplicada a um problema de Data Science. O objetivo principal foi refatorar um script de processamento de dados em Python para um **módulo robusto, testável e distribuível**, seguindo as melhores práticas de mercado e o ciclo de vida de MLOps:

## ⚙️ Arquitetura e Boas Práticas Implementadas

1.  **Modularidade e POO (Programação Orientada a Objetos):**
    * O código de limpeza e transformação foi encapsulado na classe `DataCleaner`, permitindo fácil reutilização e extensão.

2.  **Qualidade de Código e Testabilidade:**
    * Implementação completa de **Testes Unitários (`pytest`)** para garantir a integridade da lógica de negócios.
    * Rastreabilidade profissional com **Logging (`logging`)** para depuração e monitoramento em ambiente de produção.

3.  **Infraestrutura e Configuração:**
    * Gerenciamento de Configurações via **Variáveis de Ambiente (`.env`)**, desacoplando o código dos parâmetros de execução.
    * Pipeline de **Integração Contínua (CI/CD)** com **GitHub Actions** para automatizar os testes em cada Pull Request.

4.  **Deployment:**
    * Preparação para distribuição como um pacote Python instalável (definido via `pyproject.toml`), facilitando a instalação via `pip install`.

O resultado é um módulo de processamento de dados que garante **manutenibilidade, confiança** e está pronto para ser integrado em ambientes de produção.

## 📁 Estrutura do Projeto

O projeto adota uma estrutura modular e profissional, garantindo a separação de preocupações e a facilidade de distribuição:

* **`/src`**: Contém o código-fonte da lógica de negócio encapsulada no pacote Python (`datacleaner/`).
* **`/tests`**: Contém os testes unitários (`pytest`) que garantem a integridade do código.
* **`/data`**: Contém os datasets de entrada (como o `df_teste_ci.csv`). Inclui também o script **`data_generator.py`** usado para gerar o dataset maior. **O dataset completo (`df_produtos_500k.csv`) está no `.gitignore`.**
* **`/notebooks`**: Contém os Notebooks usados para Análise Exploratória (EDA), desenvolvimento e validação da arquitetura.
* **`.github/workflows`**: Contém a configuração do Pipeline de Integração Contínua (CI/CD com GitHub Actions).

  
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

A arquitetura do `DataCleaner` foi desenvolvida com foco em **Manutenibilidade, Testabilidade e Produção (MLOps)**, aplicando as seguintes técnicas:

| Categoria | Conceito | Aplicação |
| :--- | :--- | :--- |
| **DESIGN DE CÓDIGO** | **Modularidade (POO)** | Criação da classe `DataCleaner` (`/src`) para Encapsulamento de estado (`self.df`) e Separação de Preocupações. |
| **DESIGN DE CÓDIGO** | **API Avançada** | Uso de **`@classmethod`** (`from_csv`) e **`@staticmethod`** para melhor usabilidade, além de `*args`/`**kwargs` para extensibilidade. |
| **DESIGN DE CÓDIGO** | **Padronização** | Uso de **Type Hinting** e **Docstrings NumPy Style** em toda a classe para clareza e autogeração de documentação. |
| **QUALIDADE/TESTES** | **TESTES UNITÁRIOS** | Cobertura de código garantida pelo **`pytest`**, utilizando *Fixtures* e *Assertions* robustas. |
| **QUALIDADE/TESTES** | **RASTREABILIDADE** | Uso do módulo **`logging`** para rastrear o fluxo de execução e erros, essencial em ambientes de produção. |
| **INFRAESTRUTURA** | **CONFIGURAÇÃO** | Gerenciamento de variáveis de ambiente (e.g., `DATA_FILE_NAME`) via **`python-dotenv`**, desacoplando o código da infraestrutura. |
| **INFRAESTRUTURA** | **INTEGRAÇÃO CONTÍNUA** | Pipeline **CI/CD** configurado com **GitHub Actions** para rodar testes automaticamente em cada `push` e `PR`. |
| **INFRAESTRUTURA** | **EMPACOTAMENTO** | Preparação para distribuição como pacote Python (definido em **`pyproject.toml`**), permitindo instalação via `pip install`. |
