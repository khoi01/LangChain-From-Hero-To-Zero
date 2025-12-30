from langchain_openai import AzureChatOpenAI
from src.config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_AD_TOKEN,
)

def make_azure_chat():
    # If you use api-key auth:
    if AZURE_OPENAI_API_KEY:
        return AzureChatOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,
            api_version=AZURE_OPENAI_API_VERSION,
            azure_deployment=AZURE_OPENAI_DEPLOYMENT,
            temperature=0,
        )

    # If you use AAD token auth (advanced):
    if AZURE_OPENAI_AD_TOKEN:
        return AzureChatOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            azure_ad_token=AZURE_OPENAI_AD_TOKEN,
            api_version=AZURE_OPENAI_API_VERSION,
            azure_deployment=AZURE_OPENAI_DEPLOYMENT,
            temperature=0,
        )

    raise ValueError("Azure OpenAI credentials not set (api key or AAD token).")
