# AI Interview Prep Assistant

An AI-powered interview preparation assistant built using LangChain and Gemini AI.  
The application generates required technical skills and interview questions based on a given job role using sequential AI chains.

---

# Features

- Generates job-specific technical skills
- Creates technical interview questions automatically
- Uses Sequential Chains with LCEL
- Dynamic prompt engineering using PromptTemplate
- Structured AI workflow using LangChain

---

# Technologies Used

- Python
- LangChain
- Gemini AI
- LCEL (LangChain Expression Language)
- PromptTemplate
- StrOutputParser
- python-dotenv

---

# Project Workflow

1. User provides a job role
2. AI generates required technical skills
3. Generated skills are passed to another chain
4. AI creates interview questions based on those skills

---

# Run The Project

```bash
python3 main.py
```

---

# Sample Input

```text
Agentic AI Developer
```

---

# Sample Output

The system generated:
- Technical skills required for the role
- 15 technical interview questions related to:
  - ReAct Pattern
  - LangGraph
  - Vector Databases
  - Async orchestration
  - Tool calling
  - RAG systems
  - AI agent observability
  - Prompt injection security

---

# Output Screenshot

![Output](output/output.png)

---

# Future Improvements

- Streamlit UI integration
- Resume-based interview generation
- Voice interview simulation
- RAG-based company-specific interview preparation
- Multi-agent interview evaluation system



