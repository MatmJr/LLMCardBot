import openai
import json
from dotenv import load_dotenv
from src.models.functions.functions import funcoes_disponiveis
from src.models.tools.tools import descriptions

client = openai.Client()


def geracao_texto(
    mensagens
):
    """
    Gera texto baseado nas mensagens fornecidas, utilizando um modelo de linguagem.

    Args:
        mensagens (list): Lista de mensagens no formato [{'role': 'user'/'assistant', 'content': 'mensagem'}].
                         Define o contexto e o conteúdo da conversa.
        model (str, optional): Nome do modelo de linguagem a ser utilizado.
        max_tokens (int, optional): Número máximo de tokens que o modelo pode gerar em uma resposta.
        temperature (float, optional): Parâmetro que controla a criatividade do modelo.
                                       Valores mais baixos tornam o texto mais determinístico,
                                       enquanto valores mais altos aumentam a aleatoriedade.

    Returns:
        str: Texto gerado pelo modelo com base nas mensagens fornecidas.

    Raises:
        ValueError: Caso os parâmetros sejam inválidos ou mensagens estejam em formato inadequado.

    Example:
        mensagens = [{'role': 'user', 'content': 'Explique a teoria da relatividade.'}]
        resposta = geracao_texto(mensagens)
    """

    resposta = client.chat.completions.create(
        messages=mensagens,
        model="gpt-4o-mini",
        temperature=0,
        max_tokens=1000,
        stream=True
    )

    resposta_completa = ''

    for streaming_resposta in resposta:
        texto = streaming_resposta.choices[0].delta.content
        if texto:
            resposta_completa += texto

    return resposta_completa
