# Structured AI Output Analyzer

An AI-powered structured response analyzer built using LangChain, Gemini AI, and Pydantic Output Parsers.  
The project converts unstructured AI-generated text into clean, structured, validated outputs including summaries, pros, cons, and sentiment tone classification.

---

# Features

- Structured AI response generation
- Pydantic-based output validation
- Summary extraction
- Pros and cons analysis
- Tone classification
- Prompt engineering with format instructions
- Dynamic structured parsing using LangChain

---

# Technologies Used

- Python
- LangChain
- Gemini AI
- Pydantic
- PydanticOutputParser
- PromptTemplate
- LCEL (LangChain Expression Language)
- python-dotenv

---

# Project Workflow

1. User provides a topic or text prompt
2. PromptTemplate generates structured instructions
3. Gemini AI produces a response
4. PydanticOutputParser validates and structures output
5. Final response includes:
   - Summary
   - Pros
   - Cons
   - Tone classification

---

# Run The Project

```bash
python3 main.py
```

---

# Example Input

```text
Explain about LangChain, pros and cons
```

---

# AI Structured Output Generated

The system generated:

## Summary
- Overview of LangChain framework
- AI orchestration explanation
- LLM application workflow concepts

## Pros
- Modular architecture
- Large ecosystem support
- Simplifies RAG implementation
- Strong community support

## Cons
- Steep learning curve
- Debugging complexity
- Documentation fragmentation
- Potential over-engineering for simple projects

## Tone Classification
- Warm

---

# Pydantic Structured Parsing

The project uses:
- BaseModel
- Field validation
- Literal type restrictions
- Structured schema enforcement

This ensures reliable and validated AI outputs.

---

# Output Screenshot

![Output](output/output.png)

---

# Future Improvements

- JSON export support
- API deployment with FastAPI
- Multi-format structured outputs
- Streamlit frontend integration
- Database storage for AI responses
- Sentiment score visualization



