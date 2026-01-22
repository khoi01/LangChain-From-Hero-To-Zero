from langchain_ollama import ChatOllama
from src.config import OLLAMA_BASE_URL, OLLAMA_MODEL

def make_ollama_chat():
    return ChatOllama(base_url=OLLAMA_BASE_URL, model=OLLAMA_MODEL, temperature=0)
