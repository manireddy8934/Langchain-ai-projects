import os
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain.messages import HumanMessage,SystemMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from pydantic import BaseModel,Field
from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser
from typing import Literal



load_dotenv()

# print(os.getenv("api_key"))

llm = GoogleGenerativeAI(model="gemini-3-flash-preview",google_api_key=os.getenv('api_key'))


strout=StrOutputParser()




prompt = PromptTemplate(          #---prompttemplate without partial variable
    template ="""
    you are a career expert,
    based on the given job role :{job_role},
    lisy out 5 to 6 required skills for this job role in bullet points
    """,
    input_variables=['job_role']
)

prompt_question = PromptTemplate(          #---prompttemplate without partial variable
    template ="""
    based on the skills : {skills}
    generate 15 technical questions in a ordered list format
    """,
    input_variables=['skills']
)


# =======    chains ===============

chain_skills = prompt | llm | strout  # chain1
chain_questions = prompt_question | llm | strout   # chain2


final_chain = chain_skills | chain_questions              #  sequential chains


result = final_chain.invoke({
    'job_role' : "Agentic AI Developer "
    ''
})

final_chain.get_graph().print_ascii()            # grandalf

print(result)



