from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/main")
def read_root(query: Optional[str]):
    return {"message": f"Hi {query}"}
