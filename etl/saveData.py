from sqlalchemy import create_engine
import pymysql
import sqlite3


def salvar_mysql(df, db_host, db_user, db_password, db_name, nome_tabela):
    """
    Método para salvar o DataFrame em um banco de dados MySQL na AWS.
    """
    if df is not None:
        try:
            # Conectar ao banco MySQL no RDS e salvar o DataFrame
            engine = create_engine(
                f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
            )
            df.to_sql(nome_tabela, engine, if_exists="replace", index=False)
            print(
                f'Dados salvos na tabela "{nome_tabela}" do banco de dados MySQL "{db_name}".'
            )
        except Exception as e:
            print("Erro ao salvar os dados no banco de dados MySQL:", e)
    else:
        print("Nenhum dado para salvar no banco de dados MySQL.")


def salvar_sqlite(df, nome_tabela):
    """
    Método para salvar o DataFrame transformado em um banco de dados SQLite.
    """
    nome_banco = "datasets/Data.db"
    if df is not None:
        try:
            conexao = sqlite3.connect(nome_banco)
            df.to_sql(nome_tabela, conexao, if_exists="replace", index=False)
            conexao.close()
            print(
                f'Dados salvos na tabela "{nome_tabela}" do banco de dados "{nome_banco}".'
            )
        except Exception as e:
            print("Erro ao salvar os dados no banco de dados SQLite:", e)
    else:
        print("Nenhum dado para salvar no banco de dados.")
