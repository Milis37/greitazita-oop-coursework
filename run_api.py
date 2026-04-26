from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

from greitazita.aijus import GreitaZitaAI     
from greitazita.database import DatabaseManager
from greitazita.file_exportas import FinanceFileManager

app = FastAPI(title="GreitaZita AI Back-end", version="1.0")

# CORS – leidžia Front_Endas.html kalbėtis su backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    salon_id: int
    message: str

class FinanceOperation(BaseModel):
    salon_id: int
    type: str          # "earning" arba "expense"
    amount: float
    category: str
    description: str = ""

ai_instance = GreitaZitaAI()
db = DatabaseManager()
file_mgr = FinanceFileManager()

@app.post("/chat")
async def chat(request: ChatRequest):
    response = ai_instance.process_message(request.salon_id, request.message)
    db.save_chat_message(
        salon_id=request.salon_id,
        user_message=request.message,
        ai_response=response
    )
    return {"response": response, "status": "success"}

@app.post("/add_finance")
async def add_finance(operation: FinanceOperation):
    # Sukuriame tekstinę žinutę AI apdorojimui
    message = f"{operation.type} {operation.amount} {operation.category} {operation.description}"
    
    # Apdorojame per AI (išlaikome visus OOP + Builder)
    response = ai_instance.process_message(operation.salon_id, message)
    
    # Struktūrizuotas įrašas CSV
    record = {
        'type': operation.type,
        'amount': operation.amount,
        'category': operation.category,
        'description': operation.description,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Išsaugome į CSV
    file_mgr.append_to_csv(record, f"salon_{operation.salon_id}_finance.csv")
    
    # Išsaugome į DB
    db.save_chat_message(operation.salon_id, message, response)
    
    return {
        "response": response,
        "status": "success",
        "message": "Duomenys išsaugoti į CSV ir duomenų bazę!",
        "saved_file": f"salon_{operation.salon_id}_finance.csv"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
