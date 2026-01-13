Below is a **structured LangChain learning roadmap** written in **Markdown**, explicitly aligned to the **Docker + Jupyter + LangChain project structure** you just set up.
This roadmap is optimized for **hands-on training**, **progressive complexity**, and **clean separation of concerns**—the same design principles you already apply in your RAG work.

---

# LangChain Learning Roadmap

**Environment:** Docker + JupyterLab
**Target:** OpenAI, Azure OpenAI, Ollama (local)
**Outcome:** Production-ready LangChain usage with LCEL, RAG, and agentic patterns

---

## Phase 0 – Environment & Mental Model (Foundation)

### Objective

Understand **what LangChain is** and **where it fits** in an LLM system before writing complex chains.

### Concepts

* What LangChain **is NOT** (not an LLM, not a vector DB)
* LangChain as **orchestration layer**
* Difference between:

  * Prompt engineering
  * Chain composition
  * Retrieval augmentation
* Why LCEL exists (declarative, composable pipelines)

### Hands-on

* Run `docker compose up`
* Open JupyterLab
* Execute a single `llm.invoke("Hello")`

### Files Used

```
Exercises/00_foundations/0.0_sanity_check.ipynb
src/config.py
src/llms/openai_chat.py
```

### Exit Criteria

* You can switch between OpenAI, Azure, and Ollama by changing only `.env`
* You understand where credentials live and why notebooks stay clean

---

## Beginner Level – Core LangChain Primitives

> Focus: **Deterministic chains, not “AI magic”**

---

## 1. Prompt → LLM → Output (The Simplest Chain)

### Concepts

* `ChatOpenAI`, `AzureChatOpenAI`, `ChatOllama`
* `invoke()` vs `stream()`
* Temperature and determinism

### Hands-on

Notebook:

```
Exercises/01_beginner/1.2_openai_chat.ipynb
```

Implement:

```python
prompt = "Explain LCEL in 3 bullet points"
llm.invoke(prompt)
```

### Outcome

You understand:

* LLM is just a callable function
* No “chain” yet—just controlled inference

---

## 2. Prompt Templates

### Concepts

* `ChatPromptTemplate`
* Variable injection
* Why hardcoded prompts don’t scale

### Hands-on

Create:

```
Exercises/01_beginner/2.2_prompt_templates.ipynb
```

Example:

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} to a {audience}"
)
```

### Outcome

* Prompts become reusable components
* Clear separation of prompt vs execution

---

## 3. Output Parsers

### Concepts

* Why raw text is dangerous in pipelines
* `StrOutputParser`
* Structured outputs (preview only)

### Hands-on

```
Exercises/01_beginner/03_output_parsers.ipynb
```

Chain:

```python
prompt | llm | StrOutputParser()
```

### Outcome

* You can safely consume LLM outputs in code

---

## Intermediate Level – LCEL & Retrieval Foundations

> Focus: **Composable pipelines and data grounding**

---

## 4. LangChain Expression Language (LCEL)

### Concepts

* Why LCEL replaced legacy `Chain` classes
* Pipe operator (`|`)
* Declarative execution graphs

### Hands-on

```
Exercises/02_intermediate/2.1_lcel_basics.ipynb
```

Example:

```python
chain = prompt | llm | parser
chain.invoke({"topic": "RAG"})
```

### Outcome

* You think in **pipelines**, not functions
* Easy debugging and recomposition

---

## 5. Document Loaders & Text Splitters

### Concepts

* Loaders vs splitters
* Why chunking strategy affects recall
* Fixed vs structure-aware chunking

### Hands-on

```
Exercises/02_intermediate/11_document_ingestion.ipynb
```

Use:

* `TextLoader`
* `RecursiveCharacterTextSplitter`

### Outcome

* You understand ingestion ≠ retrieval
* Chunk size becomes a design decision

---

## 6. Embeddings & Vector Stores

### Concepts

* What embeddings represent
* Why cosine similarity works
* Vector DB ≠ database

### Hands-on

```
Exercises/03_advanced/12_embeddings_vectorstore.ipynb
```

Use:

* `OpenAIEmbeddings` or local embedding model
* Chroma (in-memory first)

### Outcome

* You can store and retrieve semantically similar chunks

---

## 7. Basic RAG Chain

### Concepts

* Retrieve → Augment → Generate
* Context window constraints
* Why hallucinations happen

### Hands-on

```
Exercises/03_advanced/13_basic_rag.ipynb
```

Pipeline:

```
User Query
 → Retriever
 → Prompt (with context)
 → LLM
 → Parser
```

### Outcome

* You can explain RAG on a whiteboard
* You understand failure modes

---

## Advanced Level – Production Patterns & Agentic Systems

> Focus: **Control, observability, and autonomy**

---

## 8. Query Rewriting & Routing

### Concepts

* Why user queries are often bad
* Multi-query expansion
* Query intent classification

### Hands-on

```
Exercises/03_advanced/20_query_rewriting.ipynb
```

Use LLM to:

* Rewrite query
* Compare original vs rewritten results

### Outcome

* Retrieval quality improves without new data

---

## 9. Hybrid Retrieval (Keyword + Semantic)

### Concepts

* BM25 vs vector search
* When embeddings fail
* Hybrid recall strategies

### Hands-on

```
Exercises/03_advanced/21_hybrid_retrieval.ipynb
```

Combine:

* Keyword search (SQLite / FTS)
* Vector search (Chroma)

### Outcome

* You avoid over-embedding everything
* You control precision vs recall

---

## 10. Tool Calling & Function Interfaces

### Concepts

* LLMs as planners, not executors
* Tools vs chains
* Deterministic side effects

### Hands-on

```
Exercises/03_advanced/30_tool_calling.ipynb
```

Create tools:

* Search
* Database lookup
* API call

### Outcome

* LLM decisions are bounded and auditable

---

## 11. Agentic Design Patterns (Controlled Autonomy)

### Concepts

* ReAct
* Plan-Execute
* Supervisor-Worker
* When NOT to use agents

### Hands-on

```
Exercises/03_advanced/31_agent_patterns.ipynb
```

Implement:

* Single-agent planner
* Tool-using executor

### Outcome

* You can justify agents architecturally
* No infinite loops or runaway costs

---

## 12. Observability & Evaluation (Critical)

### Concepts

* Why “it feels better” is not a metric
* Retrieval distance tracking
* Prompt + context logging

### Hands-on

```
Exercises/03_advanced/40_evaluation.ipynb
```

Log:

* Query
* Retrieved chunks
* Scores
* Final answer

### Outcome

* You can explain *why* an answer was produced

---

## Final Outcome Checklist

You are **LangChain-competent** when you can:

* Switch LLM providers via `.env`
* Build LCEL pipelines without legacy chains
* Explain and tune chunking strategies
* Debug RAG failures systematically
* Decide when agents are justified
* Log and evaluate retrieval quality

---

## Recommended Study Order (Strict)

1. Prompt → LLM → Parser
2. LCEL
3. Ingestion & Chunking
4. Embeddings & Retrieval
5. RAG
6. Hybrid Search
7. Tool Calling
8. Agentic Patterns
9. Evaluation & Observability

---

If you want next:

* I can **generate all notebooks empty + scaffolded**
* Or map this roadmap **directly to your AssistanceAI RAG codebase**
* Or compress this into a **12-week study plan** with deliverables

Tell me which direction you want.
