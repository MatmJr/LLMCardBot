import json
import yfinance as yf
import openai
from dotenv import load_dotenv
from functions.functions import *
from functions.textGen import *




_ = load_dotenv()

client = openai.Client()

if __name__ == "__main__":

    print("Pergunte algo para o TickerBot ou digite sair para encerrar")
    mensagens = []
    while True:
        texto = input("User: ")
        if texto.lower() in ["sair"]:
            print("Encerrando o TickerBot. Até mais! =]")
            break
        mensagens.append({"role": "user", "content": texto})
        mensagens = geracao_texto(mensagens)
