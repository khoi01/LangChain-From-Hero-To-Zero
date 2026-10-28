<div align="center">
  <img src="assets/banner.png" width="100%" alt="LangChain Hero Banner">

  # LangChain: From Hero to Zero
  ### *Mastering RAG & Agentic AI Systems*

  [![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
  [![Docker](https://img.shields.io/badge/Docker-Container-blue?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
  [![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-orange?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com/)
  [![LangChain](https://img.shields.io/badge/LangChain-Framework-green?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com/)

  **A comprehensive guide to building production-ready Retrieval-Augmented Generation (RAG) and Agentic AI applications.**

</div>

---


## 🚀 Core Features

- **Multi-Provider Support:** Learn to orchestrate OpenAI, Azure OpenAI, and Local LLMs (Ollama).
- **LCEL Focused:** Master the LangChain Expression Language for building scalable pipes.
- **RAG Architecture:** Deep-dives into Chunking, Vector Stores, Hybrid Search, and Evaluation.
- **Agentic Patterns:** Moving from static chains to autonomous decision-making agents.
- **Production-Ready Mindset:** Insights into data residency, cost control, and hallucination defense.

---

## 📖 How to Use This Repo

This repository is split into learning tracks, each with theory and hands-on labs:

1.  **[Learning/](Learning/)** — Read `.md` lessons (LangChain, LangGraph, Machine Learning).
2.  **[Exercises/](Exercises/)** — Run matching `.ipynb` notebooks.

**Machine Learning track:** [Learning/MachineLearning/roadmap.md](Learning/MachineLearning/roadmap.md)

**Learning Path:**
1. Start in the `Learning` folder to read the documentation for a specific module.
2. Open the matching file in the `Exercises` folder to practice.
3. If you want to dive deeper or review a concept after a session, return to the `Learning` folder.

---

## 🛠️ Deployment Guide

Run the whole repo (LangChain, LangGraph, and Machine Learning notebooks) in Docker. The image installs **both** dependency files:

| File | Purpose |
|------|---------|
| [requirements.txt](requirements.txt) | Jupyter, LangChain, RAG, FastAPI, Ollama clients |
| [requirements-ml.txt](requirements-ml.txt) | NumPy, Pandas, scikit-learn, XGBoost, PyTorch, etc. |

The [Dockerfile](Dockerfile) runs `pip install -r requirements.txt -r requirements-ml.txt` at build time. Your project folder is mounted at `/app`, so code and notebooks stay in sync with your machine.

### 1. Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
- Clone this repository and `cd` into the repo root.

### 2. Environment setup
Copy the example env file and edit secrets:

```bash
cp .env.example .env
```

Minimum variables for Jupyter and LLM exercises (see [.env.example](.env.example) for the full list):

```env
# OpenAI / Azure (LangChain track)
OPENAI_API_KEY=your_key_here
AZURE_OPENAI_API_KEY=your_key_here
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/

# Ollama — use the Docker service name from inside notebooks
OLLAMA_BASE_URL=http://ollama:11434
OLLAMA_MODEL=llama3.2

# JupyterLab login token (required by docker-compose)
JUPYTER_TOKEN=your_secure_password
```

### 3. Build and run

**First time or after changing `requirements.txt` / `requirements-ml.txt` / `Dockerfile`:**

```bash
docker compose build --no-cache
docker compose up -d
```

**Everyday start (image already built):**

```bash
docker compose up -d
```

**Open JupyterLab:** [http://localhost:8888](http://localhost:8888) — sign in with the `JUPYTER_TOKEN` from `.env`.

**Check containers:**

```bash
docker compose ps
docker compose logs -f lab
```

**Stop:**

```bash
docker compose down
```

### 4. Verify Python packages (optional)

LangChain + ML stack inside the running lab container:

```bash
docker exec -it langchain-lab python -c "
import langchain, sklearn, pandas, torch
print('langchain', langchain.__version__)
print('sklearn', sklearn.__version__)
print('pandas', pandas.__version__)
print('torch', torch.__version__)
"
```

Quick ML smoke test: open [Exercises/MachineLearning/00_foundations/0.0_ml_sanity_check.ipynb](Exercises/MachineLearning/00_foundations/0.0_ml_sanity_check.ipynb) in Jupyter and run all cells.

### 5. When you change dependencies

1. Edit [requirements.txt](requirements.txt) and/or [requirements-ml.txt](requirements-ml.txt).
2. Rebuild the image (step 3 above). A volume mount alone does **not** install new pip packages into the container.
3. If you need a one-off install without rebuilding (not recommended long term):

   ```bash
   docker exec -it langchain-lab pip install -r /app/requirements.txt -r /app/requirements-ml.txt
   ```

### 6. Local Python (without Docker)

If you prefer a venv on the host instead of Docker:

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt -r requirements-ml.txt
jupyter lab
```

Use `OLLAMA_BASE_URL=http://localhost:11434` when Ollama runs on your machine (not `http://ollama:11434`).

### 7. Ollama local LLM setup
Since the environment runs in Docker, you need to download (pull) the models into the Ollama container before first use.

**Download Default Model (`llama3.2`):**
```bash
docker exec -it ollama ollama pull llama3.2
```

**Download Other Models:**
You can download any model from the [Ollama Library](https://ollama.com/library):
```bash
docker exec -it ollama ollama pull mistral
docker exec -it ollama ollama pull phi3
```

**Verify Downloaded Models:**
```bash
docker exec -it ollama ollama list
```

---

## 📚 Course Syllabus

### 🏁 Phase 0: Foundations
- [0.0 Getting Started](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/Langchain/00_foundations/0.0_getting_started.md) - The Mental Model & Setup.
- [1.1 Mental Model](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/Langchain/00_foundations/1.1_mental_model.md) - Why LangChain?

### 🟢 Level 1: Beginner (Model Orchestration)
- [1.2 OpenAI Chat](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/Langchain/01_beginner/1.2_openai_chat.md) | [Exercise](file:///e:/Github/LangChain-From-Hero-To-Zero/Exercises/Langchain/01_beginner/1.2_openai_chat.ipynb)
- [1.3 Azure OpenAI](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/Langchain/01_beginner/1.3_azure_openai.md) | [Exercise](file:///e:/Github/LangChain-From-Hero-To-Zero/Exercises/Langchain/01_beginner/1.3_azure_openai.ipynb)
- [1.4 Ollama Local](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/Langchain/01_beginner/1.4_ollama_local.md) | [Exercise](file:///e:/Github/LangChain-From-Hero-To-Zero/Exercises/Langchain/01_beginner/1.4_ollama_local.ipynb)

### 🟡 Level 2: Intermediate (LCEL & Pipelines)
- [2.1 LCEL Basics](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/Langchain/02_intermediate/2.1_lcel_basics.md) | [Exercise](file:///e:/Github/LangChain-From-Hero-To-Zero/Exercises/Langchain/02_intermediate/2.1_lcel_basics.ipynb)
- [2.2 Prompt Templates](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/Langchain/02_intermediate/2.2_prompt_templates.md) | [Exercise](file:///e:/Github/LangChain-From-Hero-To-Zero/Exercises/Langchain/02_intermediate/2.2_prompt_templates.ipynb)
- [2.3 Structured Output](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/Langchain/02_intermediate/2.3_structured_output.md)
- [2.4 Reliability](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/Langchain/02_intermediate/2.4_reliability.md)
- [2.5 Provider Routing](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/Langchain/02_intermediate/2.5_llm_router.md)

### 🔴 Level 3: Advanced (RAG & Agentic Systems)
- [3.1 RAG Basics](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/Langchain/03_advanced/3.1_rag_basics.md)
- [3.2 Vector Retrieval](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/Langchain/03_advanced/3.2_vector_retrieval.md)
- [3.3 Hybrid Search](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/Langchain/03_advanced/3.3_hybrid_search.md)
- [3.4 Chunking Strategies](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/Langchain/03_advanced/3.4_chunking_strategies.md)
- [3.5 Agents & Tools](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/Langchain/03_advanced/3.5_agents_intro.md)
- [3.6 RAG Evaluation](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/Langchain/03_advanced/3.6_rag_evaluation.md)
- [3.7 Production Migration](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/Langchain/03_advanced/3.7_prod_migration.md)

---

## 📊 Machine Learning Syllabus

Full roadmap (Phase 0 + eight categories, 100+ lessons): **[Learning/MachineLearning/roadmap.md](Learning/MachineLearning/roadmap.md)**

- **Start:** [0.0 Getting Started](Learning/MachineLearning/00_foundations/0.0_getting_started.md) · [Sanity check notebook](Exercises/MachineLearning/00_foundations/0.0_ml_sanity_check.ipynb)
- **Capstones:** [Projects/MachineLearning/](Projects/MachineLearning/)

---

## 💡 Troubleshooting
**ConnectError [Errno 111]:** This usually means you are using `localhost` instead of the Docker service name. Always use `http://ollama:11434` when connecting from a notebook in this environment.

---
*Created with ❤️ by Antigravity.*

