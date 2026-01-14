from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# ✅ CORRECT PACKAGE IMPORT
from chatbot_engine import get_response

app = FastAPI(
    title="Futurelab AI Assistant",
    description="Customer-facing AI assistant for Futurelab Studios",
    version="1.0.0",
)

# -------------------------------------------------
# CORS
# -------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------
# Schemas
# -------------------------------------------------
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

# -------------------------------------------------
# Health check
# -------------------------------------------------
@app.get("/")
def health():
    return {"status": "Futurelab AI Assistant backend running"}

# -------------------------------------------------
# Chat endpoint
# -------------------------------------------------
@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    return ChatResponse(reply=get_response(req.message))
