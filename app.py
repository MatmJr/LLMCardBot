import json
import yfinance as yf
import openai
from dotenv import load_dotenv
import streamlit as st
from src.models.functions.functions import *
from src.models.tools.tools import *
from src.models.textGen import *
from src.views.mainPage import *


_ = load_dotenv()

client = openai.Client()

if __name__ == "__main__":
        
    paginaPrincipal()        
