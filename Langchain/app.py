from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


import streamlit as st
import os
from dotenv import load_dotenv


os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"]="true"
os.envirin["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


#Prompt template

prompt=ChatPromptTemplate.from_messages(
    [
        ("sytem","You are a helpful assistant .Please answer the questions")
        ("user","Question:{question}")
    ]
)

#streamlit framework

st.title("Langchain demo app")
input_text=st.text_input("Search the topic u want")


#openai llm model

llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
