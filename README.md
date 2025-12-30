# LangChain: From Hero to Zero (RAG & Agentic AI)

Welcome to the ultimate hands-on roadmap for mastering **LangChain**, designed to take you from foundational model calls to building production-ready **RAG (Retrieval-Augmented Generation)** and **Agentic AI** systems.

This project provides a fully containerized environment (Docker + JupyterLab) and 17+ detailed tutorial modules that bridge the gap between "simple demos" and "real-world enterprise applications."

---

## 🚀 Core Features

- **Multi-Provider Support:** Learn to orchestrate OpenAI, Azure OpenAI, and Local LLMs (Ollama).
- **LCEL Focused:** Master the LangChain Expression Language for building scalable pipes.
- **RAG Architecture:** Deep-dives into Chunking, Vector Stores, Hybrid Search, and Evaluation.
- **Agentic Patterns:** Moving from static chains to autonomous decision-making agents.
- **Production-Ready Mindset:** Insights into data residency, cost control, and hallucination defense.

---

## 🛠️ Deployment Guide

### 1. Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

### 2. Environment Setup
Create a `.env` file in the root directory and add your credentials:
```env
# OpenAI / Azure
OPENAI_API_KEY=your_key_here
AZURE_OPENAI_API_KEY=your_key_here
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/

# Ollama (Internal Docker Networking)
OLLAMA_BASE_URL=http://ollama:11434
OLLAMA_MODEL=llama3.2

# Jupyter
JUPYTER_TOKEN=your_secure_password
```

### 3. Run the Environment
Launch the JupyterLab and Ollama services:
```bash
docker compose up -d
```

### 4. Manage Local Models
In this environment, you must "pull" models into the Ollama container before using them. Run these commands in your terminal:
```bash
# Pull the standard model used in Level 1.4
docker exec ollama ollama pull llama3.2

# (Optional) Pull a lightweight model
docker exec ollama ollama pull phi3
```

### 5. Access JupyterLab
Open [http://localhost:8888](http://localhost:8888) and enter your `JUPYTER_TOKEN`.

---

## 📚 Course Syllabus

### 🏁 Phase 0: Foundations
- [0.0 Getting Started](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/00_real_tutorial_start.md) - The Mental Model & Setup.

### 🟢 Level 1: Beginner (Model Orchestration)
- [1.1 Mental Model](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/1.1_mental_model.md) - Why LangChain?
- [1.2 OpenAI Chat](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/1.2_openai_chat.md) - The industry standard.
- [1.3 Azure OpenAI](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/1.3_azure_openai.md) - Enterprise reality.
- [1.4 Ollama Local](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/1.4_ollama_local.md) - Dark mode development.

### 🟡 Level 2: Intermediate (LCEL & Pipelines)
- [2.1 LCEL Basics](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/2.1_lcel_basics.md) - The pipe operator (`|`).
- [2.2 Prompt Templates](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/2.2_prompt_templates.md) - Decoupling logic.
- [2.3 Structured Output](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/2.3_structured_output.md) - Pydantic schemas.
- [2.4 Reliability](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/2.4_reliability.md) - Retries & Fallbacks.
- [2.5 Provider Routing](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/2.5_llm_router.md) - Dynamic intent.

### 🔴 Level 3: Advanced (RAG & Agentic Systems)
- [3.1 RAG Basics](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/3.1_rag_basics.md) - Hallucination defense.
- [3.2 Vector Retrieval](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/3.2_vector_retrieval.md) - Semantic search.
- [3.3 Hybrid Search](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/3.3_hybrid_search.md) - Precision + Vibe.
- [3.4 Chunking Strategies](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/3.4_chunking_strategies.md) - Parent-Document RAG.
- [3.5 Agents & Tools](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/3.5_agents_intro.md) - Autonomy.
- [3.6 RAG Evaluation](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/3.6_rag_evaluation.md) - LLM-as-a-Judge.
- [3.7 Production Migration](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/3.7_prod_migration.md) - LangServe & Scale.

---

## 💡 Troubleshooting
**ConnectError [Errno 111]:** This usually means you are using `localhost` instead of the Docker service name. Always use `http://ollama:11434` when connecting from a notebook in this environment.

---
*Created with ❤️ by Antigravity.*
