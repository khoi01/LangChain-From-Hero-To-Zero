FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# System deps (kept minimal)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Set model cache directory
ENV TRANSFORMERS_CACHE=/app/models/embeddings \
    HF_HOME=/app/models/embeddings \
    SENTENCE_TRANSFORMERS_HOME=/app/models/embeddings \
    HUGGINGFACE_HUB_CACHE=/app/models/embeddings

# Pre-download embedding model
RUN mkdir -p /app/models/embeddings && \
    python -c "from sentence_transformers import SentenceTransformer; \
    model_name = 'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'; \
    print(f'Downloading embedding model: {model_name}'); \
    SentenceTransformer(model_name, cache_folder='/app/models/embeddings'); \
    print('Model download complete.')"

# Copy project (you can also rely on volume mounts only)
COPY src /app/src
COPY Learning /app/Learning
COPY Exercises /app/Exercises

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
