import pandas as pd
from sqlalchemy import create_engine

# Função de Extração
def extrair_dados(caminho_arquivo):
    return pd.read_csv(caminho_arquivo)

# Função de Transformação
def transformar_dados(dados):
    if 'Idade' in dados.columns:
        dados['Idade'] = dados['Idade'] + 5  # Aumenta a idade em 5 anos
    else:
        print("A coluna 'Idade' não foi encontrada no DataFrame.")

    if 'Cidade' in dados.columns:
        dados['Cidade'] = dados['Cidade'].str.upper()  # Converte o nome da cidade para maiúsculas
    else:
        print("A coluna 'Cidade' não foi encontrada no DataFrame.")

    return dados

# Função de Carga em Banco de Dados
def carregar_dados_banco(dados_transformados, nome_tabela, engine):
    dados_transformados.to_sql(name=nome_tabela, con=engine, index=False, if_exists='replace')

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
