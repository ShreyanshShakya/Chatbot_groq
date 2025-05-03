import os
from dotenv import load_dotenv
from groq import Groq
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Load environment variables
load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (you can restrict this to your frontend URL)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Root route
@app.get("/")
async def root():
    return {"message": "Welcome to the Coding Chatbot API!"}

# Request model
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # Provide a programming-specific context for the chatbot
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a coding assistant. You can help with code completion, "
                        "writing new code, and generating documentation. Provide clear, "
                        "concise, and accurate responses."
                    ),
                },
                {
                    "role": "user",
                    "content": request.message,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        response = chat_completion.choices[0].message.content
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}
