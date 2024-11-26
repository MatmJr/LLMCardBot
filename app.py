import openai
from dotenv import load_dotenv
from src.models.textGen import *
from src.views.mainPage import *


_ = load_dotenv()

client = openai.Client()

if __name__ == "__main__":
        
    paginaPrincipal()        
