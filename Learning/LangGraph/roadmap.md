Below is a **structured LangGraph learning roadmap** written in **Markdown**, explicitly aligned to the **Docker + Jupyter + LangChain project structure** you already set up.
This roadmap is optimized for **hands-on training**, **progressive complexity**, and **clean separation of concerns**—building on LangChain primitives to design **stateful, controllable agent workflows**.

**Prerequisite:** Complete the [LangChain roadmap](../Langchain/roadmap.md) through LCEL, tool calling, and agentic patterns (Modules 4, 10, and 11).

---

# LangGraph Learning Roadmap

**Environment:** Docker + JupyterLab
**Target:** OpenAI, Azure OpenAI, Ollama (local)
**Outcome:** Production-ready LangGraph usage with stateful graphs, checkpointing, multi-agent orchestration, and human-in-the-loop control

---

## How to Use This Track

This track follows the same two-folder pattern as LangChain:

1. **[Learning/LangGraph/](.)** — Read the `.md` files here for concepts, mental models, examples, and the "why" behind each module.
2. **[Exercises/LangGraph/](../../Exercises/LangGraph/)** — Open the matching `.ipynb` notebooks to execute code and practice.

**Learning Path:**

1. Start in `Learning/LangGraph/` to read the documentation for a module.
2. Open the corresponding notebook in `Exercises/LangGraph/` to practice.
3. Return to the Learning folder to review concepts after each session.

---

## Phase 0 – Environment & Mental Model (Foundation)

### Objective

Understand **what LangGraph is** and **why graphs replace ad-hoc agent loops** before building multi-step workflows.

### Read

```
Learning/LangGraph/00_foundations/0.0_getting_started.md
Learning/LangGraph/00_foundations/1.1_mental_model.md
```

### Concepts

* What LangGraph **is NOT** (not a replacement for LangChain, not a new LLM)
* LangGraph as a **state machine / orchestration runtime** on top of LangChain
* Difference between LCEL chains, agent loops, and explicit graphs
* Core vocabulary: **State**, **Node**, **Edge**, **Compile**

### Hands-on

```
Exercises/LangGraph/00_foundations/0.0_graph_sanity_check.ipynb
```

* Confirm `langgraph` is installed in the Jupyter environment
* Run a minimal two-node graph: `START → greet → END`
* Compare side-by-side: LCEL chain vs. equivalent StateGraph

### Files Used

```
Learning/LangGraph/00_foundations/0.0_getting_started.md
Learning/LangGraph/00_foundations/1.1_mental_model.md
Exercises/LangGraph/00_foundations/0.0_graph_sanity_check.ipynb
src/config.py
src/llms/openai_chat.py
```

### Exit Criteria

* You can explain why a graph is better than a `while` loop for agent control
* You understand that state is explicit, typed, and inspectable at every step

---

## Beginner Level – Graph Primitives & Control Flow

> Focus: **Explicit state, deterministic routing, no magic loops**

---

## 1. Your First StateGraph (Nodes & Edges)

### Read

```
Learning/LangGraph/01_beginner/1.1_first_stategraph.md
```

### Concepts

* `StateGraph`, `START`, `END`
* Defining nodes as plain Python functions
* `graph.compile()` and `app.invoke()`
* Graph visualization with `app.get_graph().draw_mermaid_png()`

### Hands-on

```
Exercises/LangGraph/01_beginner/1.1_first_stategraph.ipynb
```

Implement:

```python
from langgraph.graph import StateGraph, START, END
from typing import TypedDict

class State(TypedDict):
    message: str

def greet(state: State) -> State:
    return {"message": f"Hello, {state['message']}!"}

graph = StateGraph(State)
graph.add_node("greet", greet)
graph.add_edge(START, "greet")
graph.add_edge("greet", END)

app = graph.compile()
app.invoke({"message": "LangGraph"})
```

### Outcome

* You understand graphs as **named steps with shared state**
* No agent loop yet—just controlled, inspectable execution

---

## 2. Typed State & Reducers

### Read

```
Learning/LangGraph/01_beginner/1.2_typed_state.md
```

### Concepts

* `TypedDict` for graph state schemas
* `Annotated` with reducers (e.g., `add_messages` for chat history)
* Partial state updates vs. full state replacement
* Why schema design matters early

### Hands-on

```
Exercises/LangGraph/01_beginner/1.2_typed_state.ipynb
```

Example:

```python
from typing import Annotated
from langgraph.graph.message import add_messages

class ChatState(TypedDict):
    messages: Annotated[list, add_messages]
```

### Outcome

* State is a **first-class contract**, not an implicit dict
* Message history appends correctly across turns

---

## 3. Conditional Edges & Routing

### Read

```
Learning/LangGraph/01_beginner/1.3_conditional_routing.md
```

### Concepts

* Fixed edges vs. conditional edges
* Router functions that return the next node name
* `END` as a valid routing target
* Building simple intent classifiers as graph routers

### Hands-on

```
Exercises/LangGraph/01_beginner/1.3_conditional_routing.ipynb
```

Example:

```python
def route_by_intent(state: ChatState) -> str:
    last = state["messages"][-1].content
    if "weather" in last.lower():
        return "weather_node"
    return "general_node"

graph.add_conditional_edges("classifier", route_by_intent)
```

### Outcome

* Control flow is **visible in the graph**, not buried in prompt logic
* You can trace exactly why a path was chosen

---

## Intermediate Level – Agents, Memory & Human Control

> Focus: **Stateful agents, persistence, and safe interruption**

---

## 4. Chatbots with Message State

### Read

```
Learning/LangGraph/02_intermediate/2.1_chatbot_graph.md
```

### Concepts

* `MessagesState` (built-in chat state)
* Binding an LLM node to append assistant replies
* Multi-turn conversations inside a single graph
* Streaming with `app.stream()`

### Hands-on

```
Exercises/LangGraph/02_intermediate/2.1_chatbot_graph.ipynb
```

Pipeline:

```
User Message
 → LLM Node
 → Updated Messages (state)
 → END (or loop for multi-turn)
```

### Outcome

* You build a conversational graph without a manual `while True` loop
* Streaming events are tied to node execution, not opaque callbacks

---

## 5. Tool Nodes & the ReAct Loop

### Read

```
Learning/LangGraph/02_intermediate/2.2_react_graph.md
```

### Concepts

* `ToolNode` and prebuilt tool execution
* `tools_condition` for routing after LLM tool calls
* ReAct as an explicit graph: `agent → tools → agent → … → END`
* Tool errors as state, not silent failures

### Hands-on

```
Exercises/LangGraph/02_intermediate/2.2_react_graph.ipynb
```

Graph shape:

```
START → agent → [tools | END]
              ↑__________|
```

Use tools from the LangChain track (`Learning/Langchain/03_advanced/3.5_agents_intro.md`).

### Outcome

* Agent loops are **bounded, visual, and debuggable**
* You can set max iterations as a graph-level guardrail

---

## 6. Checkpointing & Memory

### Read

```
Learning/LangGraph/02_intermediate/2.3_checkpointing.md
```

### Concepts

* Why stateless graphs lose context between invocations
* `MemorySaver` (in-memory checkpointer)
* `thread_id` for conversation isolation
* Reading and resuming from checkpoints

### Hands-on

```
Exercises/LangGraph/02_intermediate/2.3_checkpointing.ipynb
```

Example:

```python
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()
app = graph.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "user-123"}}
app.invoke({"messages": [("user", "Hi")]}, config)
app.invoke({"messages": [("user", "What did I just say?")]}, config)
```

### Outcome

* Conversations persist across calls without manual history management
* You understand threads as first-class session identifiers

---

## 7. Human-in-the-Loop (Interrupts)

### Read

```
Learning/LangGraph/02_intermediate/2.4_human_in_the_loop.md
```

### Concepts

* `interrupt_before` / `interrupt_after`
* Pausing execution for human approval
* Resuming with `app.invoke(None, config)` or updated state
* When to interrupt: tool calls, sensitive actions, low-confidence routes

### Hands-on

```
Exercises/LangGraph/02_intermediate/2.4_human_in_the_loop.ipynb
```

Flow:

```
Agent proposes tool call
 → Graph pauses (interrupt)
 → Human approves / edits / rejects
 → Graph resumes
```

### Outcome

* High-risk actions require explicit human consent
* You can audit proposed actions before execution

---

## Advanced Level – Multi-Agent Systems & Production

> Focus: **Composition, persistence, observability, and deployment readiness**

---

## 8. Multi-Agent Patterns (Supervisor & Handoffs)

### Read

```
Learning/LangGraph/03_advanced/3.1_multi_agent_supervisor.md
```

### Concepts

* Single graph vs. multi-agent topology
* Supervisor pattern: one router delegates to specialist nodes
* Handoff pattern: agents pass control via state updates
* When multi-agent helps vs. when it adds unnecessary complexity

### Hands-on

```
Exercises/LangGraph/03_advanced/3.1_multi_agent_supervisor.ipynb
```

Implement:

* **Supervisor node** — classifies task and routes to `researcher`, `writer`, or `reviewer`
* **Specialist nodes** — each with its own prompt and optional tools
* **Return edge** — specialists report back to supervisor or END

### Outcome

* You can justify multi-agent design on a whiteboard
* No uncontrolled agent-to-agent chatter

---

## 9. Subgraphs & Composition

### Read

```
Learning/LangGraph/03_advanced/3.2_subgraphs.md
```

### Concepts

* Subgraphs as reusable graph components
* Calling a compiled subgraph from a parent graph
* Shared vs. isolated state between parent and child
* Building a library of reusable workflow modules

### Hands-on

```
Exercises/LangGraph/03_advanced/3.2_subgraphs.ipynb
```

Compose:

* `rag_subgraph` — retrieve → generate
* `review_subgraph` — critique → revise
* `main_graph` — orchestrates both in sequence

### Outcome

* Complex workflows are built from tested, reusable pieces
* Each subgraph can be developed and debugged independently

---

## 10. Persistent Storage (Beyond MemorySaver)

### Read

```
Learning/LangGraph/03_advanced/3.3_persistent_checkpoints.md
```

### Concepts

* `SqliteSaver` for local durable checkpoints
* Postgres-backed checkpointers for production
* What gets persisted (state snapshots, metadata, thread history)
* Checkpoint retention and cleanup policies

### Hands-on

```
Exercises/LangGraph/03_advanced/3.3_persistent_checkpoints.ipynb
```

Use:

* `SqliteSaver.from_conn_string("checkpoints.db")`
* Inspect checkpoint history for a thread
* Resume a session after container restart

### Outcome

* Graph state survives process restarts
* You can replay and debug past conversation threads

---

## 11. Streaming, Async & Parallel Nodes

### Read

```
Learning/LangGraph/03_advanced/3.4_streaming_async.md
```

### Concepts

* `app.stream()` event types (`on_chain_start`, `on_tool_start`, etc.)
* `ainvoke` / `astream` for async execution
* Parallel fan-out with multiple edges from one node
* Mapping stream events to UI updates (chat, progress, tool status)

### Hands-on

```
Exercises/LangGraph/03_advanced/3.4_streaming_async.ipynb
```

Stream and log:

* Node entry / exit
* LLM token chunks
* Tool call arguments and results

### Outcome

* You can build responsive UIs on top of graph execution
* Long-running graphs provide meaningful progress feedback

---

## 12. Observability, Testing & Production Migration

### Read

```
Learning/LangGraph/03_advanced/3.5_prod_observability.md
```

### Concepts

* LangSmith tracing for graph runs (spans per node)
* Unit testing individual nodes in isolation
* Integration testing full graph paths with fixed LLM mocks
* Time travel: replaying from a specific checkpoint
* Mapping graph modules to `src/` packages for deployment

### Hands-on

```
Exercises/LangGraph/03_advanced/3.5_prod_observability.ipynb
```

Log and evaluate:

* Input state per node
* Routing decisions
* Tool calls and results
* Final output vs. expected path

### Outcome

* You can explain *why* a graph took a specific path
* Graphs are testable, traceable, and ready to extract from notebooks

---

## 📚 Course Syllabus

### 🏁 Phase 0: Foundations

- [0.0 Getting Started](00_foundations/0.0_getting_started.md) | [Exercise](../../Exercises/LangGraph/00_foundations/0.0_graph_sanity_check.ipynb)
- [1.1 Mental Model](00_foundations/1.1_mental_model.md)

### 🟢 Level 1: Beginner (Graph Primitives)

- [1.1 First StateGraph](01_beginner/1.1_first_stategraph.md) | [Exercise](../../Exercises/LangGraph/01_beginner/1.1_first_stategraph.ipynb)
- [1.2 Typed State & Reducers](01_beginner/1.2_typed_state.md) | [Exercise](../../Exercises/LangGraph/01_beginner/1.2_typed_state.ipynb)
- [1.3 Conditional Routing](01_beginner/1.3_conditional_routing.md) | [Exercise](../../Exercises/LangGraph/01_beginner/1.3_conditional_routing.ipynb)

### 🟡 Level 2: Intermediate (Agents & Memory)

- [2.1 Chatbot Graph](02_intermediate/2.1_chatbot_graph.md) | [Exercise](../../Exercises/LangGraph/02_intermediate/2.1_chatbot_graph.ipynb)
- [2.2 ReAct Graph](02_intermediate/2.2_react_graph.md) | [Exercise](../../Exercises/LangGraph/02_intermediate/2.2_react_graph.ipynb)
- [2.3 Checkpointing](02_intermediate/2.3_checkpointing.md) | [Exercise](../../Exercises/LangGraph/02_intermediate/2.3_checkpointing.ipynb)
- [2.4 Human-in-the-Loop](02_intermediate/2.4_human_in_the_loop.md) | [Exercise](../../Exercises/LangGraph/02_intermediate/2.4_human_in_the_loop.ipynb)

### 🔴 Level 3: Advanced (Multi-Agent & Production)

- [3.1 Multi-Agent Supervisor](03_advanced/3.1_multi_agent_supervisor.md) | [Exercise](../../Exercises/LangGraph/03_advanced/3.1_multi_agent_supervisor.ipynb)
- [3.2 Subgraphs](03_advanced/3.2_subgraphs.md) | [Exercise](../../Exercises/LangGraph/03_advanced/3.2_subgraphs.ipynb)
- [3.3 Persistent Checkpoints](03_advanced/3.3_persistent_checkpoints.md) | [Exercise](../../Exercises/LangGraph/03_advanced/3.3_persistent_checkpoints.ipynb)
- [3.4 Streaming & Async](03_advanced/3.4_streaming_async.md) | [Exercise](../../Exercises/LangGraph/03_advanced/3.4_streaming_async.ipynb)
- [3.5 Production & Observability](03_advanced/3.5_prod_observability.md) | [Exercise](../../Exercises/LangGraph/03_advanced/3.5_prod_observability.ipynb)

---

## Final Outcome Checklist

You are **LangGraph-competent** when you can:

* Explain the difference between LCEL chains and StateGraphs
* Design typed state schemas with appropriate reducers
* Build ReAct-style tool loops as explicit graphs with guardrails
* Persist and resume conversations with checkpointing
* Add human-in-the-loop interrupts for sensitive actions
* Compose multi-agent workflows with supervisor or handoff patterns
* Use subgraphs to modularize complex pipelines
* Stream, trace, and test graph execution systematically

---

## Recommended Study Order (Strict)

1. Read `0.0_getting_started.md` → Exercise `0.0_graph_sanity_check.ipynb`
2. Read `1.1_first_stategraph.md` → Exercise `1.1_first_stategraph.ipynb`
3. Read `1.2_typed_state.md` → Exercise `1.2_typed_state.ipynb`
4. Read `1.3_conditional_routing.md` → Exercise `1.3_conditional_routing.ipynb`
5. Read `2.1_chatbot_graph.md` → Exercise `2.1_chatbot_graph.ipynb`
6. Read `2.2_react_graph.md` → Exercise `2.2_react_graph.ipynb`
7. Read `2.3_checkpointing.md` → Exercise `2.3_checkpointing.ipynb`
8. Read `2.4_human_in_the_loop.md` → Exercise `2.4_human_in_the_loop.ipynb`
9. Read `3.1_multi_agent_supervisor.md` → Exercise `3.1_multi_agent_supervisor.ipynb`
10. Read `3.2_subgraphs.md` → Exercise `3.2_subgraphs.ipynb`
11. Read `3.3_persistent_checkpoints.md` → Exercise `3.3_persistent_checkpoints.ipynb`
12. Read `3.4_streaming_async.md` → Exercise `3.4_streaming_async.ipynb`
13. Read `3.5_prod_observability.md` → Exercise `3.5_prod_observability.ipynb`

---

## Relationship to the LangChain Track

| LangChain Module | LangGraph Module | Connection |
|---|---|---|
| [2.1 LCEL Basics](../Langchain/02_intermediate/2.1_lcel_basics.md) | 1.1 First StateGraph | Pipelines become nodes; graphs add branching and loops |
| [3.5 Agents Intro](../Langchain/03_advanced/3.5_agents_intro.md) | 2.2 ReAct Graph | Tools move into an explicit agent → tools cycle |
| [3.5 Agents Intro](../Langchain/03_advanced/3.5_agents_intro.md) | 3.1 Multi-Agent | ReAct / Plan-Execute become graph topologies |
| [3.6 RAG Evaluation](../Langchain/03_advanced/3.6_rag_evaluation.md) | 3.5 Observability | Same mindset: trace decisions, not just outputs |

Complete the LangChain track first, then follow this roadmap in order.

---

If you want next:

* I can **generate all Learning `.md` files and Exercises notebooks scaffolded**
* Or map this roadmap **directly to your AssistanceAI agent codebase**
* Or compress this into a **10-week study plan** with deliverables

Tell me which direction you want.
