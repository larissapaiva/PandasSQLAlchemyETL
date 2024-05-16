# ETL Pipeline com Pandas e SQLAlchemy

Este repositório contém um script Python para executar um processo ETL (Extração, Transformação e Carga) simples utilizando as bibliotecas Pandas e SQLAlchemy. 

## Visão Geral

O script realiza as seguintes etapas:

1. **Extração**: Lê os dados de um arquivo CSV.
2. **Transformação**: Realiza transformações específicas nos dados.
3. **Carga**: Carrega os dados transformados em um banco de dados SQLite.

## Pré-requisitos

- Python 3.6 ou superior
- Pandas
- SQLAlchemy

Você pode instalar as dependências utilizando `pip`:

```bash
pip install pandas sqlalchemy
```

## Estrutura do Código

### Importações

O script importa as bibliotecas necessárias para manipulação de dados e interação com o banco de dados:

```python
import pandas as pd
from sqlalchemy import create_engine
```

### Funções

#### Função de Extração

Esta função lê os dados de um arquivo CSV especificado e retorna um DataFrame do Pandas:

```python
def extrair_dados(caminho_arquivo):
    return pd.read_csv(caminho_arquivo)
```

#### Função de Transformação

Esta função realiza duas transformações nos dados:
1. Aumenta em 5 anos o valor da coluna `Idade`, se presente.
2. Converte os valores da coluna `Cidade` para maiúsculas, se presente.

```python
def transformar_dados(dados):
    if 'Idade' in dados.columns:
        dados['Idade'] = dados['Idade'] + 5
    else:
        print("A coluna 'Idade' não foi encontrada no DataFrame.")
    
    if 'Cidade' in dados.columns:
        dados['Cidade'] = dados['Cidade'].str.upper()
    else:
        print("A coluna 'Cidade' não foi encontrada no DataFrame.")
    
    return dados
```

#### Função de Carga

Esta função carrega os dados transformados em uma tabela de um banco de dados SQLite. Se a tabela já existir, ela será substituída:

```python
def carregar_dados_banco(dados_transformados, nome_tabela, engine):
    dados_transformados.to_sql(name=nome_tabela, con=engine, index=False, if_exists='replace')
```

### Script Principal

No bloco principal, o script executa as etapas do processo ETL:

```python
if __name__ == "__main__":
    # Caminho do arquivo de entrada
    arquivo_entrada = 'dados_originais.csv'
    
    # Caminho do banco de dados SQLite
    caminho_banco = 'sqlite:///dados.db'
    
    # Nome da tabela no banco de dados
    nome_tabela = 'dados_transformados'
    
    # Criar uma conexão com o banco de dados
    engine = create_engine(caminho_banco)
    
    # Extração de dados
    dados_extraidos = extrair_dados(arquivo_entrada)
    
    # Transformação de dados
    dados_transformados = transformar_dados(dados_extraidos)
    
    # Carga de dados no banco de dados
    carregar_dados_banco(dados_transformados, nome_tabela, engine)
    
    print("Processo ETL concluído com sucesso. Dados carregados no banco de dados.")
```

## Executando o Script

Para executar o script, basta rodar o seguinte comando no terminal:

```bash
python etl_pipeline.py
```

Certifique-se de que o arquivo CSV de entrada (`dados_originais.csv`) está no mesmo diretório que o script ou forneça o caminho correto para o arquivo.

## Contribuição

Sinta-se à vontade para abrir issues ou pull requests se tiver sugestões de melhorias ou encontrar bugs.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
