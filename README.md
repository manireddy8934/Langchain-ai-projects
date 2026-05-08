# LangChain AI Projects

A collection of AI engineering projects built using LangChain, Gemini AI, LCEL, AI agents, structured output parsing, and parallel workflows.

These projects demonstrate practical implementations of:
- Sequential Chains
- Parallel Chains
- AI Agents
- ReAct Pattern
- Structured AI Outputs
- Prompt Engineering
- Tool Calling
- Workflow Visualization

---

# Projects Included

---

# 1. AI Interview Prep Assistant

An AI-powered interview preparation assistant that generates:
- Required technical skills
- Technical interview questions
- Role-specific preparation content

## Features
- Sequential chains
- Prompt engineering
- Dynamic interview generation
- LCEL workflow chaining

## Technologies
- LangChain
- Gemini AI
- PromptTemplate
- StrOutputParser

---

# 2. Parallel Enterprise Report Analyzer

An enterprise-grade AI report analysis system that simultaneously analyzes business reports from:
- Sales perspective
- Technology perspective
- HR perspective

## Features
- RunnableParallel
- Multi-department analysis
- AI-generated business insights
- Workflow visualization

## Technologies
- LangChain
- Gemini AI
- RunnableParallel
- PromptTemplate

---

# 3. Structured AI Output Analyzer

A structured response generation system using Pydantic Output Parsers.

The project converts unstructured AI responses into validated structured outputs containing:
- Summary
- Pros
- Cons
- Tone classification

## Features
- Structured AI responses
- Pydantic validation
- Output parsing
- Schema enforcement

## Technologies
- LangChain
- Gemini AI
- Pydantic
- PydanticOutputParser

---

# 4. ReAct-Powered AI Search Agent

A real-time AI search assistant that combines:
- LLM reasoning
- External web search
- Tool execution
- ReAct agent workflows

## Features
- Tavily Search integration
- ReAct Pattern
- AI agents
- Real-time information retrieval
- Tool calling workflows

## Technologies
- LangChain
- Gemini AI
- Tavily Search
- AI Agents
- LangGraph

---

# Repository Structure

```text
LangChain_Projects/
│
├── AI-Interview-Prep-Assistant/
├── Parallel-Enterprise-Report-Analyzer/
├── Structured-AI-Output-Analyzer/
├── ReAct-Powered-AI-Search-Agent/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Technologies Used

- Python
- LangChain
- Gemini AI
- LCEL
- Prompt Engineering
- Pydantic
- Tavily Search
- AI Agents
- LangGraph
- RunnableParallel

---

# How To Run

## 1. Clone Repository

```bash
git clone https://github.com/manireddy8934/Langchain-ai-projects.git
```

---

## 2. Create Virtual Environment

```bash
python3 -m venv myenv
```

---

## 3. Activate Environment

```bash
source myenv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Create .env File

```env
api_key=YOUR_GEMINI_API_KEY
tavily_api_key=YOUR_TAVILY_API_KEY
```

---

## 6. Run Projects

```bash
python3 main.py
```

---

# Future Improvements

- RAG Applications
- Streamlit AI Dashboards
- Multi-Agent Systems
- LangGraph Workflows
- Memory-enabled AI Agents
- Vector Database Integration
- FastAPI Deployment
- Voice-enabled AI Assistants

---
