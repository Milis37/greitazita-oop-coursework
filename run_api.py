from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from greitazita.aijus import GreitaZitaAI
from greitazita.database import DatabaseManager

app = FastAPI(title="GreitaZita AI Back-end", version="1.0")

# BŪTINA — leidžia Front_Endas.html prisijungti
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    salon_id: int
    message: str

ai_instance = GreitaZitaAI()
db = DatabaseManager()

@app.post("/chat")
async def chat(request: ChatRequest):
    response = ai_instance.process_message(request.salon_id, request.message)
    
    # ✅ IŠSAUGOM į MySQL
    db.save_chat_message(
        salon_id=request.salon_id,
        user_message=request.message,
        ai_response=response
    )
    
    return {"response": response, "status": "success"}
