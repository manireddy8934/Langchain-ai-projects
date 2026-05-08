# ReAct-Powered AI Search Agent

An AI-powered real-time search assistant built using LangChain, Gemini AI, and Tavily Search.  
The project uses the ReAct (Reason + Act) agent pattern to combine LLM reasoning with external web search capabilities for answering real-time and current-event queries.

---

# Features

- Real-time web search integration
- ReAct-based AI agent workflow
- Tavily Search tool integration
- Current events information retrieval
- AI reasoning + tool execution
- External search-based response generation
- LangChain agent architecture

---

# Technologies Used

- Python
- LangChain
- Gemini AI
- Tavily Search API
- AI Agents
- ReAct Pattern
- LangGraph
- python-dotenv

---

# Project Workflow

1. User asks a real-time or current-event question
2. AI agent determines whether external search is required
3. Tavily Search tool retrieves live web information
4. Gemini AI processes retrieved data
5. Final response is generated using reasoning + search results

---

# Run The Project

```bash
python3 main.py
```

---

# Example Queries

```text
Give me information about Indigo crisis in Dec 2025
```

```text
Give me info about Claude Code of Anthropic in 2 to 3 lines
```

---

# AI Agent Capabilities

The project demonstrates:

- Tool calling
- Agent reasoning
- External search execution
- Dynamic response generation
- Real-time information retrieval
- Multi-step AI workflows

---

# Search Tool Integration

The system integrates:
- Tavily Search API
- Gemini AI model
- LangChain agents
- ReAct prompting strategy

The AI agent intelligently decides when to:
- use internal reasoning
- call external search tools
- combine retrieved information into final answers

---

# Output Screenshots

## Real-Time Search Response

![Output](output/output1.png)

---

## Agent + Tavily Search Execution

![Workflow](output/output2.png)

---

# Example Real-Time Information Retrieved

The AI agent successfully generated:
- Aviation industry crisis analysis
- Real-time airline operational disruptions
- Current AI tooling information
- Claude Code overview
- Search-based dynamic responses

---

# Future Improvements

- Multi-tool agent integration
- Memory-enabled AI agents
- Streamlit conversational UI
- Voice-enabled AI assistant
- RAG + Search hybrid architecture
- Multi-agent collaboration workflows

