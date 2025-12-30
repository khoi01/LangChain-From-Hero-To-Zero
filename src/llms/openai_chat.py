from langchain_openai import ChatOpenAI
from src.config import OPENAI_MODEL

def make_openai_chat():
    # OPENAI_API_KEY picked up automatically from env
    return ChatOpenAI(model=OPENAI_MODEL, temperature=0)
