from fastapi import FastAPI, Request 
from pydantic import BaseModel

app = FastAPI(title="FastAPI + Snyk Demo")

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI demo project!"}

@app.get("/vulnerable")
def vulnerable_endpoint(user_input: str):
    # Example of insecure code (for Snyk Code to flag)
    eval(user_input)  # ❌ Dangerous: Remote Code Execution risk
    return {"message": f"Executed: {user_input}"}


class PRData(BaseModel):
    pr_number: str
    title: str
    author: str
    branch: str

@app.post("/pr-check")
async def pr_check(pr: PRData, request: Request):
    client_host = request.client.host
    logger.info(f"PR Check received from {client_host}:- {pr.dict()}")
    
    # this is for test
    response = {
        "message": "PR data received successfully",
        "pr_number": pr.pr_number,
        "title": pr.title,
        "author": pr.author,
        "branch": pr.branch,
        "status": "ok"
    }
    return respons
