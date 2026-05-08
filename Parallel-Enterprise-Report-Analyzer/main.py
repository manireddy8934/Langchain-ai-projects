# ============  Problem Statement ===============

# Last quarter, the company launched a new mobile application. 
# The app received high user traffic, but there were frequent crashes during peak hours. 
# Customer complaints increased by 35%, and the support team reported high workload. 
# Despite technical issues, overall revenue increased by 18% due to strong marketing campaigns. 
# However, employee overtime increased, and attrition risk is rising in the engineering team.
#  Management is planning to release a major update next quarter with additional features.


import os
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain.messages import HumanMessage,SystemMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from pydantic import BaseModel,Field
from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser
from typing import Literal
from langchain_core.runnables import RunnableParallel,RunnablePassthrough,RunnableLambda


load_dotenv()

# print(os.getenv("api_key"))

llm = GoogleGenerativeAI(model="gemini-3-flash-preview",google_api_key=os.getenv('api_key'))


strout=StrOutputParser()

sales_prompt = PromptTemplate(
        template= """
        summarize the given report mainly focusing on revenue and 
        the report is :{report}
        """,
    input_variable = ['report']
)

tech_prompt = PromptTemplate(
        template= """
        summarize the given report mainly focusing on tech risk associated with it:{report}
        """,
    input_variable = ['report']
)


hr_prompt = PromptTemplate(
        template= """
        summarize the given report and 
        analyze hr and employees impact:{report}
        """,
    input_variable = ['report']
)



chain_sales = sales_prompt | llm | strout  # chain1
chain_tech = tech_prompt| llm | strout   # chain2
chain_hr = hr_prompt| llm | strout   # chain3


final_chain = RunnableParallel({
        "sales" :chain_sales,
        "tech":chain_tech,
        "hr":chain_hr
})



res = final_chain.invoke({
    "report":"""
        Last quarter, the company launched a new mobile application. 
The app received high user traffic, but there were frequent crashes during peak hours. 
Customer complaints increased by 35%, and the support team reported high workload. 
Despite technical issues, overall revenue increased by 18% due to strong marketing campaigns. 
However, employee overtime increased, and attrition risk is rising in the engineering team.
 Management is planning to release a major update next quarter with additional features.

 """

})



print(res)

final_chain.get_graph().print_ascii()