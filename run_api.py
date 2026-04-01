from fastapi import FastAPI
from pydantic import BaseModel
from greitazita.ai import GreitaZitaAI
from greitazita.database import DatabaseManager

app = FastAPI(title="GreitaZita AI Back-end", version="1.0")

class ChatRequest(BaseModel):
    salon_id: int
    message: str

ai_instance = GreitaZitaAI()
db_instance = DatabaseManager()

@app.post("/chat")
async def chat(request: ChatRequest):
    """Endpoint that poesimus.lt Jotform AI can call."""
    response = ai_instance.process_message(request.salon_id, request.message)
    return {"response": response, "status": "success"}

@app.get("/")
async def root():
    return {"message": "✅ GreitaZita Python back-end is running. Ready for poesimus.lt integration."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
