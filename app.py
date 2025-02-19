from fastapi import FastAPI
from financial_agent import multi_agent

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Kshitiz's Financial Agents API!. How can I help you"}

@app.get("/query/")
def query(message: str):
    response = multi_agent.run(message)
    return {"response": response}
