import json
import os


if __name__ == "__main__":
    with open("./AnswerBot/treinamento/chatbot_respostas.json", encoding="utf8") as f:
        json_respostas = json.load(f)

    with open(
        "./AnswerBot/treinamento/chatbot_respostas.jsonl", "w", encoding="utf8"
    ) as f:
        for entrada in json_respostas:
            resposta = {
                "resposta": entrada["resposta"],
                "categoria": entrada["categoria"],
                "fonte": "AnswerBot",
            }
            entrada_jsonl = {
                "messages": [
                    {"role": "user", "content": entrada["pergunta"]},
                    {
                        "role": "assistant",
                        "content": json.dumps(resposta, ensure_ascii=False, indent=2),
                    },
                ]
            }
            json.dump(entrada_jsonl, f, ensure_ascii=False)
            f.write("\n")
