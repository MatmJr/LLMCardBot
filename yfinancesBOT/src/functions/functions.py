import yfinance as yf
import datetime
import json


def cotacaoFechamento_acao_periodo(
    ticker,
    period
):
    """
    Obtém o histórico de cotações de fechamento de uma ação brasileira em um período especificado.

    A função utiliza a biblioteca `yfinance` para buscar os dados históricos de fechamento para 
    um determinado ticker e período. Em casos onde o número de valores retornados excede 30, 
    aplica uma limitação reduzindo a granularidade dos dados retornados.

    Parâmetros:
    ----------
    ticker : str
        O símbolo da ação no Yahoo Finance. Para ações brasileiras, deve incluir o sufixo '.SA' 
        (por exemplo, 'ABEV3.SA').
    period : str
        O período desejado para consulta (por exemplo, '1d', '5d', '1mo', '1y', etc.).

    Retorno:
    -------
    str
        Um JSON contendo o histórico de cotações de fechamento, com o índice de datas no formato 
        'YYYY-MM-DD' e os valores correspondentes às cotações de fechamento.

    Limitações:
    -----------
    - Se o número de valores retornados for superior a 30, a função reduz o conjunto de dados, 
      aplicando uma amostragem proporcional para respeitar a limitação.
    - Para ações brasileiras, o ticker deve ser especificado com o sufixo '.SA'.

    Exemplo de Uso:
    ---------------
    >>> cotacaoFechamento_acao_periodo('ABEV3.SA', '1y')
    '{"2024-11-22": 12.68, "2024-11-21": 12.50, ...}'
    """
    hist = yf.Ticker(f'{ticker}.SA').history(period=period)['Close']
    hist.index = hist.index.strftime('%Y-%m-%d')
    hist = round(hist,4)
    if len(hist) > 30:
        slice_size = int(len(hist) / 30)
        hist = hist.iloc[::-slice_size][::-1]
    return hist.to_json()

funcoes_disponiveis = {'cotacaoFechamento_acao_periodo': cotacaoFechamento_acao_periodo}