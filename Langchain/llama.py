from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set LangChain environment variables
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please answer the questions."),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.title("LangChain + Ollama Demo")
input_text = st.text_input("Enter your question:")

# Ollama model (make sure Ollama is installed and running locally)
# llm = Ollama(model="llama2")
llm = Ollama(model="phi")
output_parser = StrOutputParser()

# Create chain
chain = prompt | llm | output_parser

# Run chain when user inputs text
if input_text:
    response = chain.invoke({"question": input_text})
    st.write("### Answer:")
    st.write(response)
