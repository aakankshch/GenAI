from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.prompts import PromptTemplate 
from langchain_community.llms import Ollama  
from langchain_core.output_parsers import StrOutputParser

import streamlit as st

# streamlit framework

st.title('Celebrity Search Results')
input_text=st.text_input("Search the Formula1 Driver you want")

# Prompt Templates
input_prompt=PromptTemplate(
    template="Tell me about Formula 1 Racing celebrity {name} in 5 points and Number of Championships he has won",
    input_variables=['name']
    )

#LLM Model & Output Parser
llm = Ollama(model="llama2")
output_parser=StrOutputParser()
#Chain
chain=input_prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'name':input_text}))