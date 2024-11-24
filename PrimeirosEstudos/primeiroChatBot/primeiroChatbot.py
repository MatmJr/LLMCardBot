from dotenv import load_dotenv
import openai


# O código só vai funcionar com uma OPENAI_API_KEY válida.
_ = load_dotenv()
client = openai.Client()


def geracao_texto(mensagens, model="gpt-4o-mini", max_tokens=None, temperature=0):
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
        stream=True,
    )

    print("CreditCardBot: ", end="")
    resposta_completa = ""
    for resposta_stream in resposta:
        text = resposta_stream.choices[0].delta.content
        if text:
            print(text, end="")
            resposta_completa += text
    print()
    mensagens.append({"role": "assistant", "content": resposta_completa})
    return mensagens


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
