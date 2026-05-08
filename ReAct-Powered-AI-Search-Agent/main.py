from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from langchain.messages import SystemMessage,HumanMessage
from langchain.agents import create_agent
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
   api_key=os.getenv("api_key"),
)

res = llm.invoke("give me information about indogo crisis in dec 2025")



tavily_search=TavilySearch(
    tavily_api_key=os.getenv("TAVILY_API_KEY"),
    max_results=3,
    topic="general",
)
print(res)

res1 = tavily_search.invoke({
    "query":"give me information about indogo crisis in dec 2025"
})

print(res1)

search_agent=create_agent(
    model=llm,
    tools=[tavily_search],
    # verbose=True,
    system_prompt=SystemMessage(
        """
        you are a search assistant
        for any question related to  current events or events after jan 2025,
        you must use the search tool and answer
        dont rely on internal knowledge


        """)

)

res2=search_agent.invoke({
    "messages":[HumanMessage(
        "give me info about claude code of antropic in 2 to 3 lines "
    )]
})



print(res2["messages"][-1].content[0]["text"])
