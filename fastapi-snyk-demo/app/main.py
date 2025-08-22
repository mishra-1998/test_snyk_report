from fastapi import FastAPI

app = FastAPI(title="FastAPI + Snyk Demo")

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI demo project!"}

@app.get("/vulnerable")
def vulnerable_endpoint(user_input: str):
    # Example of insecure code (for Snyk Code to flag)
    eval(user_input)  # ❌ Dangerous: Remote Code Execution risk
    return {"message": f"Executed: {user_input}"}
