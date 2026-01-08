# LangChain: From Hero to Zero (RAG & Agentic AI)

Welcome to the ultimate hands-on roadmap for mastering **LangChain**, designed to take you from foundational model calls to building production-ready **RAG (Retrieval-Augmented Generation)** and **Agentic AI** systems.

This project provides a fully containerized environment (Docker + JupyterLab) and 17+ detailed tutorial modules organized into a leveled learning path.

---

## 🚀 Core Features

- **Multi-Provider Support:** Learn to orchestrate OpenAI, Azure OpenAI, and Local LLMs (Ollama).
- **LCEL Focused:** Master the LangChain Expression Language for building scalable pipes.
- **RAG Architecture:** Deep-dives into Chunking, Vector Stores, Hybrid Search, and Evaluation.
- **Agentic Patterns:** Moving from static chains to autonomous decision-making agents.
- **Production-Ready Mindset:** Insights into data residency, cost control, and hallucination defense.

---

## 📖 How to Use This Repo

This repository is split into two major segments to optimize your learning experience:

1.  **[Learning/](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/)**: This is your theoretical hub. Read the `.md` files here to understand concepts, mental models, and the "why" behind LangChain.
2.  **[Exercises/](file:///e:/Github/LangChain-From-Hero-To-Zero/Exercises/)**: This is your hands-on laboratory. Open the corresponding `.ipynb` notebooks to execute code and training exercises.

**Learning Path:**
1. Start in the `Learning` folder to read the documentation for a specific module.
2. Open the matching file in the `Exercises` folder to practice.
3. If you want to dive deeper or review a concept after a session, return to the `Learning` folder.

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

---

## 📚 Course Syllabus

### 🏁 Phase 0: Foundations
- [0.0 Getting Started](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/00_foundations/0.0_getting_started.md) - The Mental Model & Setup.
- [1.1 Mental Model](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/00_foundations/1.1_mental_model.md) - Why LangChain?

### 🟢 Level 1: Beginner (Model Orchestration)
- [1.2 OpenAI Chat](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/01_beginner/1.2_openai_chat.md) | [Exercise](file:///e:/Github/LangChain-From-Hero-To-Zero/Exercises/01_beginner/1.2_openai_chat.ipynb)
- [1.3 Azure OpenAI](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/01_beginner/1.3_azure_openai.md) | [Exercise](file:///e:/Github/LangChain-From-Hero-To-Zero/Exercises/01_beginner/1.3_azure_openai.ipynb)
- [1.4 Ollama Local](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/01_beginner/1.4_ollama_local.md) | [Exercise](file:///e:/Github/LangChain-From-Hero-To-Zero/Exercises/01_beginner/1.4_ollama_local.ipynb)

### 🟡 Level 2: Intermediate (LCEL & Pipelines)
- [2.1 LCEL Basics](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/02_intermediate/2.1_lcel_basics.md) | [Exercise](file:///e:/Github/LangChain-From-Hero-To-Zero/Exercises/02_intermediate/2.1_lcel_basics.ipynb)
- [2.2 Prompt Templates](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/02_intermediate/2.2_prompt_templates.md) | [Exercise](file:///e:/Github/LangChain-From-Hero-To-Zero/Exercises/02_intermediate/2.2_prompt_templates.ipynb)
- [2.3 Structured Output](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/02_intermediate/2.3_structured_output.md)
- [2.4 Reliability](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/02_intermediate/2.4_reliability.md)
- [2.5 Provider Routing](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/02_intermediate/2.5_llm_router.md)

### 🔴 Level 3: Advanced (RAG & Agentic Systems)
- [3.1 RAG Basics](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/03_advanced/3.1_rag_basics.md)
- [3.2 Vector Retrieval](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/03_advanced/3.2_vector_retrieval.md)
- [3.3 Hybrid Search](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/03_advanced/3.3_hybrid_search.md)
- [3.4 Chunking Strategies](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/03_advanced/3.4_chunking_strategies.md)
- [3.5 Agents & Tools](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/03_advanced/3.5_agents_intro.md)
- [3.6 RAG Evaluation](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/03_advanced/3.6_rag_evaluation.md)
- [3.7 Production Migration](file:///e:/Github/LangChain-From-Hero-To-Zero/Learning/03_advanced/3.7_prod_migration.md)

---

## 💡 Troubleshooting
**ConnectError [Errno 111]:** This usually means you are using `localhost` instead of the Docker service name. Always use `http://ollama:11434` when connecting from a notebook in this environment.

---
*Created with ❤️ by Antigravity.*

