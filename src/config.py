import os
from dotenv import load_dotenv

load_dotenv()

def env(key: str, default: str | None = None) -> str | None:
    return os.getenv(key, default)

ENV = env("ENV", "dev")

# OpenAI
OPENAI_API_KEY = env("OPENAI_API_KEY")
OPENAI_MODEL = env("OPENAI_MODEL", "gpt-4o-mini")

# Azure OpenAI
AZURE_OPENAI_ENDPOINT = env("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = env("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_API_VERSION = env("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
AZURE_OPENAI_DEPLOYMENT = env("AZURE_OPENAI_DEPLOYMENT")

AZURE_OPENAI_AD_TOKEN = env("AZURE_OPENAI_AD_TOKEN")  # optional

# Ollama
OLLAMA_BASE_URL = env("OLLAMA_BASE_URL", "http://ollama:11434")
OLLAMA_MODEL = env("OLLAMA_MODEL", "llama3.1:8b-instruct")
