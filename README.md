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
- (Optional) [Ollama](https://ollama.com/) if you want to run models locally outside of Docker.

### 2. Environment Setup
Create a `.env` file in the root directory and add your credentials:
```env
OPENAI_API_KEY=your_key_here
AZURE_OPENAI_API_KEY=your_key_here
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
JUPYTER_TOKEN=your_secure_password
```

### 3. Run the Environment
Launch the JupyterLab and Ollama services:
```bash
docker compose up -d
```

### 4. Access JupyterLab
Open your browser and navigate to:
[http://localhost:8888](http://localhost:8888)
*(Enter the `JUPYTER_TOKEN` you set in `.env`)*

---

## 📚 Course Syllabus

Each module is located in the `tutorial/` directory and follows a strict: **Introduction → Objective → Concept → Example → Real-World Context → Did You Know** format.

### 🏁 Phase 0: Foundations
- [0.0 Getting Started](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/00_real_tutorial_start.md) - The Mental Model & Setup.

### 🟢 Level 1: Beginner (Model Orchestration)
- [1.1 Mental Model](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/1.1_mental_model.md) - Why LangChain?
- [1.2 OpenAI Chat](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/1.2_openai_chat.md) - The industry standard.
- [1.3 Azure OpenAI](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/1.3_azure_openai.md) - Enterprise reality.
- [1.4 Ollama Local](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/1.4_ollama_local.md) - Dark mode development.

### 🟡 Level 2: Intermediate (LCEL & Pipelines)
- [2.1 LCEL Basics](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/2.1_lcel_basics.md) - The pipe operator (`|`).
- [2.2 Prompt Templates](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/2.2_prompt_templates.md) - Decoupling logic from prose.
- [2.3 Structured Output](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/2.3_structured_output.md) - Pydantic schemas.
- [2.4 Reliability](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/2.4_reliability.md) - Retries & Fallbacks.
- [2.5 Provider Routing](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/2.5_llm_router.md) - Dynamic intent detection.

### 🔴 Level 3: Advanced (RAG & Agentic Systems)
- [3.1 RAG Basics](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/3.1_rag_basics.md) - The RAG Triad.
- [3.2 Vector Retrieval](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/3.2_vector_retrieval.md) - Geometric search.
- [3.3 Hybrid Search](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/3.3_hybrid_search.md) - String precision + Vector vibe.
- [3.4 Chunking Strategies](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/3.4_chunking_strategies.md) - Parent-Document retrieval.
- [3.5 Agents & Tools](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/3.5_agents_intro.md) - Autonomy through tool-calling.
- [3.6 RAG Evaluation](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/3.6_rag_evaluation.md) - LLM-as-a-Judge.
- [3.7 Production Migration](file:///e:/Github/LangChain-From-Hero-To-Zero/tutorial/3.7_prod_migration.md) - LangServe & Deployment.

---

## 📈 Roadmap for Success

1. **Start with 1.1** to understand the "LangChain Way."
2. **Setup your `.env`** and verify your connection in a notebook.
3. **Build your first RAG** in Level 3.
4. **Evaluate everything**—never trust an unmeasured LLM!

---
*Created with ❤️ by Antigravity.*
