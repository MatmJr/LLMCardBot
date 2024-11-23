import openai
import json
from dotenv import load_dotenv
from functions.functions import funcoes_disponiveis
from tools.tools import descriptions

client = openai.Client()

def geracao_texto(mensagens, model="gpt-4o-mini", max_tokens=1000, temperature=1, tools = descriptions):
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
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        tools=descriptions,
        tool_choice='auto'
    )

    print("TickerBot: ", end="")
    tool_calls = resposta.choices[0].message.tool_calls
    mensagens.append(resposta.choices[0].message)
    if tool_calls:
        for tool_call in tool_calls:
            func_name = tool_call.function.name
            function_to_call = funcoes_disponiveis[func_name]
            func_args = json.loads(tool_call.function.arguments)
            func_return = function_to_call(func_args['ticker'], func_args['periodo'])
            mensagens.append({
                'tool_call_id': tool_call.id,
                'role': 'tool',
                'name': func_name,
                'content': func_return
            })
        segunda_resposta = client.chat.completions.create(
            messages=mensagens,
            model='gpt-3.5-turbo-0125',
        )
        mensagens.append(segunda_resposta.choices[0].message)
    
    print(mensagens[-1].content, end='')
    print()

    return mensagens