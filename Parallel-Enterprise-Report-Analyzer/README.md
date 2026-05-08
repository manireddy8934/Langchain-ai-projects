# Parallel Enterprise Report Analyzer

An AI-powered enterprise report analysis system built using LangChain and Gemini AI.  
The project analyzes a business report simultaneously from multiple organizational perspectives including Sales, Technology, and Human Resources using parallel AI chains.

---

# Features

- Parallel report analysis using RunnableParallel
- Department-wise AI insights generation
- Revenue and sales impact analysis
- Technical risk assessment
- HR and employee impact analysis
- Workflow visualization using LangChain graph structure

---

# Technologies Used

- Python
- LangChain
- Gemini AI
- RunnableParallel
- PromptTemplate
- StrOutputParser
- LCEL (LangChain Expression Language)
- python-dotenv

---

# Project Workflow

1. Business report is provided as input
2. Three AI chains run simultaneously:
   - Sales Analysis Chain
   - Technology Risk Chain
   - HR Impact Chain
3. AI generates department-specific summaries
4. Workflow graph visualization is displayed

---

# Run The Project

```bash
python3 main.py
```

---

# Business Problem Statement

The project analyzes a real-world enterprise scenario involving:

- Mobile application launch
- High user traffic
- Frequent crashes during peak hours
- Increased customer complaints
- Revenue growth
- Engineering team burnout
- Employee attrition risks

---

# AI Analysis Generated

## Sales Analysis
- Revenue growth analysis
- Marketing campaign impact
- Customer complaint insights

## Technology Risk Analysis
- Scalability risks
- Infrastructure instability
- System architecture concerns
- Feature creep risks

## HR Impact Analysis
- Burnout detection
- Attrition risk analysis
- Employee workload impact
- Work-life balance concerns

---

# LangChain Workflow Visualization

The project visualizes parallel chain execution using LangChain graph representation.

The architecture contains:
- Multiple PromptTemplates
- Parallel AI execution
- Independent department analysis chains
- Shared input processing

---

# Output Screenshots

## Business Analysis Output

![Output](output/output1.png)

---

## Parallel Workflow Graph

![Workflow](output/output2.png)

---

# Future Improvements

- Streamlit dashboard integration
- PDF report upload support
- Real-time analytics dashboard
- Sentiment analysis integration
- RAG-based enterprise knowledge system
- Multi-agent business decision system



