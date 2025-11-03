from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM  # Updated package
from langserve import add_routes
import uvicorn
from dotenv import load_dotenv

# Load environment variables from .env (optional)
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="This is a Langchain server using FastAPI and Langserve"
)

# Initialize Ollama LLM (local model)
llm = OllamaLLM(model="phi")  # make sure 'phi' is installed locally

# Define prompt templates
prompt1 = ChatPromptTemplate.from_template("Tell me a joke about {subject}")
prompt2 = ChatPromptTemplate.from_template("Tell me a sad story about {subject}")

# Add routes for chains
add_routes(
    app,
    prompt1 | llm,
    path="/p1"
)
add_routes(
    app,
    prompt2 | llm,
    path="/p2")

# Run server
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
