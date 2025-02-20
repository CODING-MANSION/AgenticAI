from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from financial_agent import multi_agent

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://coding-mansion.github.io"],  # Allow only GitHub Pages frontend
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to the Kshitiz's Financial Agents API!. How can I help you"}

@app.get("/query/")
def query(message: str):
    response = multi_agent.run(message).content
    return {"response": response}
