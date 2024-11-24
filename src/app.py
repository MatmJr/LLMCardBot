import json
import yfinance as yf
import openai
from dotenv import load_dotenv
from models.functions.functions import *
from models.tools.tools import *
from models.textGen import *


_ = load_dotenv()

client = openai.Client()

if __name__ == "__main__":

    print("Pergunte algo para o CreditCardBot ou digite sair para encerrar")
    mensagens = []
    while True:
        texto = input("User: ")
        if texto.lower() in ["sair"]:
            print("Encerrando o CreditCardBot. Até mais! =]")
            break
        mensagens.append({"role": "user", "content": texto})
        mensagens = geracao_texto(mensagens)
