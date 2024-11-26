descriptions = [
    {
        "type": "function",
        "function": {
            "name": "cotacaoFechamento_acao_periodo",
            "description": 'Usa a "yfinance" para retornar a cotação de uma ação brasileira em um período determinado',
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string",
                        "description": 'O ticker da acao. Exemplo: "ABEV3" para ambev, "PETR4" para petrobras, etc',
                    },
                    "periodo": {
                        "type": "string",
                        "description": "O periodo analisado, Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max",
                        "enum": [
                            "1d",
                            "5d",
                            "1mo",
                            "3mo",
                            "6mo",
                            "1y",
                            "2y",
                            "5y",
                            "10y",
                            "ytd",
                            "max",
                        ],
                    },
                },
            },
        },
    }
]
