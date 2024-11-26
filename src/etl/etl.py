import pandas as pd
import requests
from io import BytesIO
import gzip
import os
from saveData import *
from dotenv import load_dotenv

# load_dotenv()
# db_host = os.getenv("db_host")
# db_name = os.getenv("db_name")
# db_user = os.getenv("db_user")
# db_password = os.getenv("db_password")

directory = "datasets"


if not os.path.exists(directory):
    os.makedirs(directory)

# URL do arquivo
url = "https://github.com/Neurolake/challenge-data-scientist/blob/main/datasets/credit_01/train.gz?raw=true"

# Fazendo o download do arquivo .gz
response = requests.get(url)
response.raise_for_status()  # Verifica se houve erro na requisição

# Abrindo o conteúdo do arquivo .gz
with gzip.open(BytesIO(response.content)) as gz:
    # Carregando o conteúdo em um DataFrame do Pandas
    df = pd.read_csv(gz)

print(df)
# Filtrando apenas as colunas necessárias
columns_of_interest = [
    "REF_DATE",
    "TARGET",
    "VAR2",
    "IDADE",
    "VAR4",
    "VAR5",
    "VAR8"
]
df_filtered = df[columns_of_interest]

try:
    df_filtered['REF_DATE'] = pd.to_datetime(df_filtered['REF_DATE'],  errors='coerce')
    print("Conversão de 'REF_DATE' concluída.")
except Exception as e:
    print(f"Erro na conversão de 'REF_DATE': {e}")
    
df_filtered['IDADE'] = df_filtered['IDADE'].fillna(df_filtered['IDADE'].median())
df_filtered = df_filtered.fillna('naoInformado')

salvar_sqlite(df_filtered, "ccdataset")
#df_filtered.to_csv('datasets/ccdataset')
#salvar_mysql(df_filtered, db_host, db_user, db_password, db_name, 'ccdata')
    




