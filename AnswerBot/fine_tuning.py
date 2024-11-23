import openai
from dotenv import load_dotenv
import json

_ = load_dotenv()

client = openai.Client()

if __name__ == "__main__":   
    
    file = openai.files.create(
        file = open('./AnswerBot/treinamento/chatbot_respostas.jsonl', 'rb'),
        purpose = 'fine-tune'
    )

    client.fine_tuning.jobs.create(
        training_file = file.id,
        model = "gpt-3.5-turbo"
    )