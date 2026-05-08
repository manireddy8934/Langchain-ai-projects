from langchain_google_genai import GoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate

from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser
from typing import Literal

load_dotenv()

llm = GoogleGenerativeAI(model="gemini-3-flash-preview", google_api_key=os.getenv("api_key"))

strout =StrOutputParser()
# summary : summary of the answer
# pros:
# cons:

class summarypydan(BaseModel):
    summary:str=Field(description="summary of the text")
    pros:str=Field(description="Positives of the text")
    cons:str=Field(description="negatives of the text")
    tone:Literal["warm","harsh"]=Field(description="Overall tone of the text") # Literal used to restrict a variable to specific fixed values only
    

parser_out =PydanticOutputParser(pydantic_object =summarypydan)


# # prompt=PromptTemplate(
# #     template="Provide simple explanation for the {task}",
# #     input_variables=["task"]

# # )

# --- Partial variables ------- (Static & Dynamic)
prompt=PromptTemplate (
    #---tone is static variable , task is dynamic variable
    input_variables=["text"],
    template ='''
    give the answer for {text} and return the following things as given
    in pydantic
    summary : a breif summary
    pros:positives
    cons:negatives
    provide the output in the format of {format_instructions}
    ''',
    partial_variables ={

        "format_instructions":parser_out.get_format_instructions()
    
    }


)

#------------- Simple Chain -------------
chains = prompt | llm | parser_out     # | = lcel (langchain exp language)

res =chains.invoke("explain about langchain, pros and cons")
print(res)






#outputparsers - they get the response give from llm and change it fixed it (givr the fixed output instaed of changing the output everytime )


# chains.get_graph().print_ascii() # grandalf
# #-------------  Chains -------------


#------  Pydantic --------------  ( when we use pydantic we have to write partial variables)

# class Pydantc(BaseModel):
#     summary: str
#     count: int

# #implicit conversation and explicit conversation
# g = Pydantc(summary="hello",count="1")

# print(g)


# class name(BaseModel):
#     a:str
#     b:int
#     c:bool

# h=name(a="a",b=3,c=True)

# print(h)